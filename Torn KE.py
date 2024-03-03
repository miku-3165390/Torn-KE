import keyboard
import time
import random
import pyautogui

def paste_and_enter():
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.1)  # Adjust this sleep time if needed
    pyautogui.press('enter')

def toggle():
    global running
    if not running:
        print("Keyboard emulation started.")
        time.sleep(1)  # Wait x seconds before toggling on
        running = True
        pyautogui.press('backspace')
        paste_and_enter()
    else:
        print("Keyboard emulation stopped.")
        time.sleep(1)  # Wait x seconds before toggling off
        running = False
        pyautogui.press('backspace')
        
keyboard.add_hotkey('=', toggle)

running = False

while True:
    if running:

        delay = random.randint(120,180)
        time.sleep(delay)

        paste_and_enter()
    else:
        time.sleep(0.1)  # Short sleep when the program is not running to avoid high CPU usage
#Made by miku [3165390]
        
#THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#DEALINGS IN THE SOFTWARE.
