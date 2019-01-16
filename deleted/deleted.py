'''
        else:
            irc.send('PRIVMSG BanchoBot stats '.encode() + Player.encode() + ' \r\n'.encode())
            for Check in range(10):
                if not Recive:
                    break
                    loop.close()
                OnlineSt = Recive.find('Idle:')
                PlaySt = Recive.find('Playing:')
                MapSt = Recive.find('Editing:')
                ModSt = Recive.find('Modding:')
                TestSt = Recive.find('Testing:')
                AfkSt = Recive.find('Afk:')
                if OnlineSt != -1:
                    await bot.send_message(Player + ' just Online!')
                    loop.close()
                    break
                else:
                    if PlaySt != -1:
                        await bot.send_message(Player + ' just Playing!')
                        loop.close()
                        break
                    else:
                        if MapSt != -1:
                            await bot.send_message(Player + ' just Editing!')
                            loop.close()
                            break
                        else:
                            if ModSt != -1:
                                await bot.send_message(Player + ' just Modding!')
                                loop.close()
                                break
                            else:
                                if TestSt != -1:
                                    await bot.send_message(Player + ' just Testing the map!')
                                    loop.close()
                                    break
                                else:
                                    if AfkSt != -1:
                                        await bot.send_message(Player + ' just AFK!')
                                        loop.close()
                                        break
                                    else:
                                        if Check == 9 | (TestSt == 0 & ModSt == 0 & MapSt == 0 & TestSt == 0 & OnlineSt == 0 & PlaySt == 0): # double check \\ on test
                                            await bot.send_message(Player + ' Offline :(')
                                            Recive = None
                                            loop.close()
                                            break
'''