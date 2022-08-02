import os
def base_path():
    current_file = os.path.realpath(__file__)
    current_file_path = "/".join(os.path.dirname(current_file).split("\\")[:-1])
    return current_file_path

def resource_path(file_name):
    current_file_path = base_path()
    resource_path =os.path.join(current_file_path,'app/resources/', file_name)
    resource_path = resource_path.replace("\\", "/")
    return resource_path

def ui_path(file_name):
    current_file_path = base_path()
    resource_path =os.path.join(current_file_path,'app/ui/', file_name)
    resource_path = resource_path.replace("\\", "/")
    return resource_path


