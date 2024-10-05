import os 
import psutil
import shutil

def clean_files_in_folder(folder_path):#will delete files
    try:
        for filename in os.listdir(folder_path):
            file_path= os.path.join(folder_path,filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        print(f"cleared : {folder_path}")

    except Exception as e:
        print(f"Failed to clear {folder_path}. Reason: {e}")

def clear_temp_file():#will delete temp files

    temp_folders=[
        os.getenv('TEMP'),
        os.getenv('TMP'),
        os.path.join(os.getenv('SystemRoot'),'Temp')
    ]

    # Add Your custom paths here
    custom_temp_folders = [
        #in case you have some other folders to managea; add there path hare 
    ]

    temp_folders.extend(custom_temp_folders)

    for folder in temp_folders:
        if folder and os.path.exists(folder):
            clean_files_in_folder(folder)


def clear_browser_cache(browser):
    cache_path = {
        'chrome':os.path.join(os.getenv('LOCALAPPDATA'),'Google','Chrome','User Data','Default','Cache'),
        'firefox': os.path.join(os.getenv('APPDATA'), 'Mozilla', 'Firefox', 'Profiles'),
        'brave': os.path.join(os.getenv('LOCALAPPDATA'), 'BraveSoftware', 'Brave-Browser', 'User Data', 'Default', 'Cache'),
        'edge': os.path.join(os.getenv('LOCALAPPDATA'), 'Microsoft', 'Edge', 'User Data', 'Default', 'Cache')
    }
    
    if browser in cache_path:
        if browser == 'firefox':
            for root, dirs, files in os.walk(cache_path[browser]):
                for dir in dirs:
                    if dir.endswith('.default-release'):
                        clean_files_in_folder(os.path.join(root, dir , 'cache2', 'enteries' ))
    
    else:
        clean_files_in_folder(cache_path[browser])


def terminate_browser_if_running(browser):
    terminated = False
    for process in psutil.process_iter(['name']):
        if browser.lower() in process.info['name'].lower():
            print(f"Terminating {process.info['name']} process...")
            process.terminate()
            terminated = True
    return terminated

                    

def main():
    print("Starting PC cleaning---")

    clear_temp_file()

    browsers = ['chrome', 'firefox', 'brave', 'edge' ]
    for browser in browsers:
        if terminate_browser_if_running(browser):
            print(f"{browser.capitalize()} was running and has been terminated")
        clear_browser_cache(browser)


    print("PC cleanup completed.")

if __name__ == "__main__":
    main()

