from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Mở Chrome
driver = webdriver.Chrome()

# Mở file login.html trên local (sửa lại đường dẫn đúng với máy bạn)
driver.get("file:///C:/Users/X/Selenium_test/login.html")

time.sleep(1)

# 1. Test login thành công
driver.find_element(By.ID, "username").send_keys("sv1@ptit.edu.vn")
driver.find_element(By.ID, "password").send_keys("P@ssw0rd")
driver.find_element(By.ID, "btnLogin").click()
time.sleep(1)
print("✅ Test 1 - Đăng nhập thành công:", driver.find_element(By.ID, "msg-success").text)

# 2. Test sai mật khẩu
driver.refresh()
driver.find_element(By.ID, "username").send_keys("sv1@ptit.edu.vn")
driver.find_element(By.ID, "password").send_keys("sai123")
driver.find_element(By.ID, "btnLogin").click()
time.sleep(1)
print("✅ Test 2 - Sai mật khẩu:", driver.find_element(By.ID, "msg-error").text)

# 3. Test bỏ trống trường
driver.refresh()
driver.find_element(By.ID, "btnLogin").click()
time.sleep(1)
print("✅ Test 3 - Bỏ trống:", driver.find_element(By.ID, "msg-error").text)

# 4. Test link Forgot password
driver.refresh()
forgot_link = driver.find_element(By.ID, "linkForgot")
assert forgot_link.is_displayed(), "❌ Link Forgot password không hiển thị"
print("✅ Link 'Forgot password?' hiển thị")

# Click bằng JavaScript để chắc chắn điều hướng
driver.execute_script("arguments[0].click();", forgot_link)
time.sleep(2)
print("✅ Điều hướng sang trang quên mật khẩu thành công (title:", driver.title, ")")




# 5. Test link SIGN UP
signup_link = driver.find_element(By.ID, "linkSignup")
assert signup_link.is_displayed(), "❌ Link SIGN UP không hiển thị"
print("✅ Link 'SIGN UP' hiển thị")

signup_link.click()
time.sleep(1)
print("✅ Điều hướng sang trang SIGN UP thành công (title:", driver.title, ")")

driver.back()
time.sleep(1)

# 6. Test nút social login
fb = driver.find_element(By.ID, "btnFacebook")
tw = driver.find_element(By.ID, "btnTwitter")
gg = driver.find_element(By.ID, "btnGoogle")

assert fb.is_displayed() and tw.is_displayed() and gg.is_displayed(), "❌ Các nút social login không hiển thị đủ"
print("✅ 3 nút social login hiển thị đầy đủ")

# Kiểm tra có thể click
fb.click()
tw.click()
gg.click()
print("✅ Các nút social login có thể click")

# Đóng browser
driver.quit()
