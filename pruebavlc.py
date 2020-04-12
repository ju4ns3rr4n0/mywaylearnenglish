import vlc
Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new('prueba.mp4')
#Sub = player.add_slave(player,'Test.srt', True)

player.set_media(Media)
player.play()
