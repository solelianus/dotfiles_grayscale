-- General options
vim.opt.clipboard = "unnamedplus"
vim.opt.number = true
vim.opt.relativenumber = true
vim.opt.termguicolors = true
vim.opt.cursorline = true
vim.opt.expandtab = true
vim.opt.shiftwidth = 4
vim.opt.tabstop = 4

-- Remove ugly ~ on empty lines
vim.opt.fillchars = { eob = " " }

-- Persistent undo across sessions
vim.opt.undofile = true
vim.opt.undodir = vim.fn.stdpath("data") .. "/undo"
