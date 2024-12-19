from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import re


def automate_quso_ai_video_generation():
    # Setup Chrome WebDriver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True) 
    
    # Configure downloads directory
    download_dir = "/path/to/downloads_directory"  
    print(f"Download Directory: {download_dir}")  
    options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        # 1. Navigate to quso.ai and maximize window
        driver.get("https://quso.ai/")
        driver.maximize_window()
        time.sleep(2)

        # 2. Find and click Login button
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'login-navbar')]"))
        )
        login_button.click()
        time.sleep(2)

        # 3. Switch to login page (new tab)
        driver.switch_to.window(driver.window_handles[-1])
        
        # 4. Click "Continue with Email" button
        continue_with_email_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "auth-email-password-btn"))
        )
        continue_with_email_button.click()
        time.sleep(2)

        # 5. Enter email
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='e.g johndoe@gmail.com']"))
        )
        email_input.send_keys("vikram0812+intern@proton.me")
        time.sleep(1)

        # 6. Enter password
        password_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']")
        password_input.send_keys("Intern@2024")
        time.sleep(1)

        # 7. Click Log in button
        login_submit_button = driver.find_element(By.ID, "login-with-email-btn")
        login_submit_button.click()
        time.sleep(3)

        # 8. Navigate to AI Video Generator
        ai_video_generator = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'AI Video Generator')]"))
        )
        ai_video_generator.click()
        time.sleep(2)

        # 9. Generate AI Script
        generate_ai_script = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "text-to-video-ai-generated-script"))
        )
        generate_ai_script.click()
        time.sleep(2)

        # 10. Enter script description
        script_textarea = driver.find_element(By.XPATH, "//textarea[@placeholder='Briefly summarize your script in a few words or sentences...']")
        script_textarea.send_keys("Create an engaging marketing video showcasing innovative tech solutions for small businesses.")
        time.sleep(1)

        # 11. Click Continue button
        continue_button = driver.find_element(By.ID, "describe-script-continue-button")
        continue_button.click()
        time.sleep(5)

        # 12. Click "Generate Script" button
        generate_script_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "text-to-video-generate-video-button"))
        )
        generate_script_button.click()
        time.sleep(5)

        # 13. Click "Generate Video" button
        generate_video_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "text-to-video-generate-video-button"))
        )
        generate_video_button.click()
        
        # 14. Wait for video processing to complete
        print("Waiting for video processing...")
        
        try:
            # Try to get processing percentage
            processing_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'text-xs') and contains(text(), 'done')]"))
            )
            processing_text = processing_element.text
            print(f"Current processing status: {processing_text}")
            
            # Extract percentage using regex
            match = re.search(r'(\d+)%', processing_text)
            if match:
                percentage = int(match.group(1))
                if percentage == 100:
                    print("Video processing completed.")
                else:
                    print("Falling back to 30-second wait...")
                    time.sleep(30)
            else:
                print("Falling back to 30-second wait...")
                time.sleep(30)
        
        except Exception as e:
            print(f"Could not retrieve processing status. {e}")
            print("Falling back to 30-second wait...")
            time.sleep(30)

        # 15. Navigate to Recent Projects
        view_all_projects = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "view-all-projects"))
        )
        view_all_projects.click()
        time.sleep(2)

        # 16. Find and click the latest project using the specific project card HTML
        latest_project = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'group relative flex h-[220px]')][1]"))
        )
        latest_project.click()
        time.sleep(3)

        # 17. Download the video
        download_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "text-to-video-download-button"))
        )
        download_button.click()
        
        print("Video download initiated.")
        time.sleep(30)  # Wait for download to complete

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Optional: Keep browser open for manual inspection
        input("Press Enter to close the browser...")
        driver.quit()

# Run the automation
if __name__ == "__main__":
    automate_quso_ai_video_generation()
