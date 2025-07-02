# Waybar Khal

Simple waybar module that formats a [khal](https://github.com/pimutils/khal)
calendar into a tooltip. Heavy inspiration taken from the
[Next calendar events](https://gist.github.com/bjesus/178a9bd3453470d74803945dbbf9ed40)
module.

![image](https://github.com/user-attachments/assets/02f6adec-2389-4b91-8ca4-6226db19f58b)

Default config:

- Events included in the nexy 14 days
- Calendar size set to 1 month in ~/.config/khal/config

```
# ~/.config/khal/config
[view]
min_calendar_display = 1
``` 

## Installation

- Clone waybar-khal.py to whereever you keep your waybar modules e.g.
`~/.config/waybar/modules/waybar-khal.py`
- Make `waybar-khal.py` executable:

```bash
chmod +x ~/.config/waybar/modules/waybar-khal.py
```

- Add the following to your waybar config

```json
"custom/khal": {
        "format": "{}",
        "tooltip": true,
        "interval": 60,
        "format-icons": {
            "default": ""
        },
        //! replace with your waybar-khal.py path
        "exec": "~/.config/waybar/modules/waybar-khal.py",
        "return-type": "json"
    },
```

- Reload waybar

## ToDo

- Find a useful way to display any events / tasks on current day
