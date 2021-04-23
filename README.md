# 👀 LCP24-100Q

Creating a class for controlling PWM controller, LCP24-100Q

> [LCP24-100Q](http://lfine.co.kr/home/%EC%A1%B0%EB%AA%85%EC%A0%9C%EC%96%B4%EA%B8%B0/?pageid=2&uid=28&mod=document)

##  Getting Started
### Development Environment
- Windows10
- vscode

> Not required

### Prerequisites
- python3
- `pip install pyserial`

### Installing
- `git clone https://github.com/sina-Kim/LCP24-100Q.git`
- or download `LCP24_100Q.py` file

## Example of use
```python
from LCP24_100Q import LCP24_100Q

device = LCP24_100Q(port='COM2')  # Check your device manager.
if device.is_open():
    for brightness in range(device.MIN_BRIGHTNESS, device.MAX_BRIGHTNESS+1,50):
        device.set_brightness('0', brightness)
        device.set_brightness('1', brightness)
        device.set_brightness('2', brightness)
        device.set_brightness('3', brightness)
        time.sleep(1)
device.close()
```
