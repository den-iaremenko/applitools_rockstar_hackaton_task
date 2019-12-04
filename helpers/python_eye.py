import cv2 as cv
import numpy as np
import asyncio

from loguru import logger


class PythonEye:

    def __init__(self, driver):
        self.driver = driver

    async def loc(self, tem, seconds=5, threshold=0.9, frequency=1):
        results_file = "verified_elements/" + tem.split("/")[-1]
        while seconds > 0:
            logger.info(f"[{seconds}] Searching for {tem}")
            screen = self.driver.save_screenshot('screen.png')
            img_rgb = cv.imread("screen.png")
            img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
            template = cv.imread(tem, 0)
            w, h = template.shape[::-1]
            res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
            loc = np.where(res >= threshold)
            if len(loc[0]) > 0 and screen:
                for pt in zip(*loc[::-1]):
                    x = int((pt[0] + (pt[0] + w)) / 2)
                    y = int((pt[1] + (pt[1] + h)) / 2)
                logger.info(f"{tem.split('/')[1]} X:Y - {x}:{y}")
                up_corner = (int(pt[0]), int(pt[1]))
                down_corner = (int(pt[0] + w), int(pt[1] + h))
                cv.rectangle(img_rgb, up_corner, down_corner, (0, 0, 255), 5)
                cv.line(img_rgb, (x, y), (x + 1, y + 1), (0, 0, 255), 20)
                cv.imwrite(results_file, img_rgb)
                return {"n": tem, "c": [x, y]}
            else:
                seconds -= frequency
                await asyncio.sleep(frequency)
        else:
            error = "Element - " + str(tem.split("/")[-1]) + " is not Found on the screen"
            return {"error": error}

    # Async task runner to find multiple objects at the same time
    def verify_objects(self, lst, sec=4, threshold=0.95, frequency=1):
        lst_of_coordinates = []
        tasks = []
        errors = []
        n = 0
        ioloop = asyncio.new_event_loop()
        logger.info(f"List of templates {str(lst)}")
        for i in lst:
            tasks.append(
                ioloop.create_task(self.loc(i, seconds=sec,
                                            threshold=threshold,
                                            frequency=frequency)))
        done, _ = ioloop.run_until_complete(asyncio.wait(tasks))
        for fut in done:
            if fut.result():
                lst_of_coordinates.append(fut.result())
        ioloop.close()
        for result in lst_of_coordinates:
            if result.get("error"):
                error_message = f"{n}.{result.get('error')} \n"
                errors.append(error_message)
                logger.error(error_message )
                n += 1
        if n > 0:
            raise AssertionError("".join(errors))
        return lst_of_coordinates
