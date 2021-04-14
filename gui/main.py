import wx
from .dialogs import AboutDialog


class MenuBar(wx.MenuBar):
    class EventHandlers:
        OnOpen = None
        OnSave = None
        OnClose = None
        OnExit = None
        OnAbout = None

    def __init__(self, handlers: EventHandlers):
        super().__init__()

        fileMenu = wx.Menu()
        openItem = fileMenu.Append(wx.ID_OPEN, '&Open\tCtrl-O', 'Open journal database')
        saveItem = fileMenu.Append(wx.ID_SAVE, '&Save\tCtrl-S', 'Save journal database')
        closeItem = fileMenu.Append(wx.ID_CLOSE, '&Close\tCtrl-W', 'Close journal database')
        fileMenu.AppendSeparator()
        exitItem = fileMenu.Append(wx.ID_EXIT)

        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        self.Append(fileMenu, '&File')
        self.Append(helpMenu, '&Help')

        self.Bind(wx.EVT_MENU, handlers.OnOpen, openItem)
        self.Bind(wx.EVT_MENU, handlers.OnSave, saveItem)
        self.Bind(wx.EVT_MENU, handlers.OnClose, closeItem)
        self.Bind(wx.EVT_MENU, handlers.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, handlers.OnAbout, aboutItem)


class MainFrame(wx.Frame):

    def __init__(self):
        super().__init__(None, title='Secreto')

        menuBarEventHandlers = MenuBar.EventHandlers()
        menuBarEventHandlers.OnOpen = self.OnOpen
        menuBarEventHandlers.OnAbout = self.OnAbout
        menuBarEventHandlers.OnExit = self.OnExit
        self.menuBar = MenuBar(menuBarEventHandlers)
        self.SetMenuBar(self.menuBar)

        self.CreateStatusBar()
        self.SetStatusText('Welcome to Secreto!')

    def OnOpen(self, evt):
        pass

    def OnAbout(self, evt):
        aboutDialog = AboutDialog(self)
        aboutDialog.Show()

    def OnExit(self, evt):
        self.Close()
