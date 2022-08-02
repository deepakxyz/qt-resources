import os
def resource_path(file_name):
    current_file = os.path.realpath(__file__)
    current_file_path = "/".join(os.path.dirname(current_file).split("\\")[:-1])
    resource_path = os.path.join(current_file_path, "qt/resources", file_name)
    return resource_path


