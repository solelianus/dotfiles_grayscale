-- Apply grayscale overrides
local function set_grayscale()
  vim.cmd([[
    hi Normal guibg=#f0f0f0 guifg=#222222
    hi LineNr guifg=#888888 guibg=#f0f0f0
    hi CursorLineNr guifg=#000000 guibg=#d6d6d6
    hi Visual guibg=#bbbbbb
    hi StatusLine guibg=#e0e0e0 guifg=#222222
    hi VertSplit guibg=#f0f0f0 guifg=#bbbbbb
    hi Pmenu guibg=#e6e6e6 guifg=#222222
    hi PmenuSel guibg=#bbbbbb guifg=#000000
    hi Search guibg=#d6d6d6 guifg=#000000
  ]])
end

vim.api.nvim_create_autocmd("ColorScheme", { callback = set_grayscale })
vim.api.nvim_create_autocmd("VimEnter", { callback = set_grayscale })

