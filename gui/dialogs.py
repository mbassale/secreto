from datetime import date
import wx.adv


class AboutDialog:

    def __init__(self, parent=None):
        self.parent = parent
        self.info = wx.adv.AboutDialogInfo()
        self.info.SetName('Secreto')
        self.info.SetVersion('Version 0.1')
        self.info.SetDescription('Cryptographic journal & diary application.')
        today = date.today()
        self.info.SetCopyright(f'(C) {today.year} Marco Bassaletti <bassaletti@gmail.com>')

    def Show(self):
        wx.adv.AboutBox(self.info, self.parent)
