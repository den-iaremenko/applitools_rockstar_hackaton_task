import glob


class TemplatesDiscoverer:

    def __init__(self, folder):
        self.folder = folder

    def get_all_templates(self):
        all_templates = [template for template in glob.glob(self.folder + "/*")]
        return all_templates
