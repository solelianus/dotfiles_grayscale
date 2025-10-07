-- Leader key
vim.g.mapleader = " "

-- Example keymaps
local keymap = vim.keymap.set
keymap("n", "<leader>ff", "<cmd>Telescope find_files<cr>", { desc = "Find files" })
keymap("n", "<leader>fg", "<cmd>Telescope live_grep<cr>", { desc = "Live grep" })
keymap("n", "<leader>e", "<cmd>NvimTreeToggle<cr>", { desc = "Toggle file explorer" })

