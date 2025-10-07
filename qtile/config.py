from libqtile import bar, layout, widget, hook
from libqtile.config import Key, Screen, Group
from libqtile.lazy import lazy
from qtile_extras import widget as extra_widget
import os

mod = "mod4"
terminal = "kitty"
rofi = "rofi -show drun"

keys = [
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "r", lazy.spawn(rofi)),
    Key([mod], "e", lazy.spawn("dolphin")),
    Key([mod], "q", lazy.window.kill()),
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([], "F1", lazy.spawn("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle")),  # Mute toggle
    Key([], "F2", lazy.spawn("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-")),  # Volume Down
    Key([], "F3", lazy.spawn("wpctl set-volume -l 1.0 @DEFAULT_AUDIO_SINK@ 5%+")),  # Volume Up

    ]

groups = [Group(i) for i in "123456789"]
for g in groups:
    keys.append(Key([mod], g.name, lazy.group[g.name].toscreen()))
    keys.append(Key([mod, "shift"], g.name, lazy.window.togroup(g.name)))

layout_theme = dict(
    border_width=2,
    margin=8,
    border_focus="#222222",
    border_normal="#d6d6d6"
)

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
]

widget_defaults = dict(font="JetBrainsMono Nerd Font", fontsize=12, padding=4)
colors = {
    "bg": "#f0f0f0",
    "fg": "#222222",
    "accent": "#666666",
    "inactive": "#bbbbbb",
}

screens = [
    Screen(
        wallpaper='/home/solelianus/Pictures/Wallpaper/(re)acquaint (Final).png',
        wallpaper_mode='fill',
        top=bar.Bar(
            [
                widget.GroupBox(
                    highlight_method="block",
                    this_current_screen_border=colors["accent"],
                    inactive=colors["inactive"],
                    active=colors["fg"],
                    rounded=False,
                    hide_unused=True,
                    padding=5,
                ),
                widget.Spacer(),
                widget.Clock(format='%H:%M %d/%m/%y', foreground=colors["fg"], fmt='<b>{}</b>'),
                widget.Spacer(),
                widget.PulseVolume(
                    check_mute_command="wpctl get-volume @DEFAULT_AUDIO_SINK@ | grep -q MUTED",
                    limit_max_volume=True,
                    foreground=colors["fg"],
                    ),
                widget.Systray(),
                ],
            26,
            background=colors["bg"],
            margin=[4,4,0,4],
        ),
    ),
]

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    os.system(home)

