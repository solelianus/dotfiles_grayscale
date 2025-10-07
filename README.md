dotfiles_grayscale
├─ laptop_wayland/   → for Intel laptop running Hyprland (Wayland)
│  ├─ hyprland/      → Hyprland config
│  ├─ waybar/        → Waybar config + style
│  ├─ kitty/         → Kitty terminal config
│  ├─ rofi/          → Rofi launcher theme
│  └─ nvim/          → Neovim (lazy.nvim) setup
│
└─ desktop_xorg/     → for NVIDIA desktop running Qtile (Xorg)
   ├─ qtile/         → Qtile config.py
   ├─ picom/         → Picom compositor config (rounded, blur)
   ├─ kitty/         → Kitty config (same look)
   ├─ rofi/          → Rofi theme (same style)
   └─ nvim/          → same Neovim config

After placing these folders:

    cp -r dotfiles_grayscale/* ~/.config/

For Qtile:
    picom --daemon --config ~/.config/picom/picom.conf

For Hyprland:
    hyprland
