#configuration
base_url = "https://home-assistant.local/"
hass_api_token = "home assistant api token"
discord_bot_token = "bot token"
entity_id = "light.bulb"
entity_name = "Entity Name"

#imports
import requests
import discord
import json
import asyncio


def run_bot(auth):
    # vars
    colors = (
        'AliceBlue', 'AntiqueWhite', 'Aqua', 'Aquamarine', 'Azure', 'Beige', 'Bisque', 'Black', 'BlanchedAlmond',
        'Blue',
        'BlueViolet', 'Brown', 'BurlyWood', 'CadetBlue', 'Chartreuse', 'Chocolate', 'Coral', 'CornflowerBlue',
        'Cornsilk',
        'Crimson', 'Cyan', 'DarkBlue', 'DarkCyan', 'DarkGoldenrod', 'DarkGray', 'DarkGreen', 'DarkGrey', 'DarkKhaki',
        'DarkMagenta', 'DarkOliveGreen', 'DarkOrange', 'DarkOrchid', 'DarkRed', 'DarkSalmon', 'DarkSeaGreen',
        'DarkSlateBlue', 'DarkSlateGray', 'DarkSlateGrey', 'DarkTurquoise', 'DarkViolet', 'DeepPink', 'DeepSkyBlue',
        'DimGray', 'DodgerBlue', 'FireBrick', 'FloralWhite', 'ForestGreen', 'Fuchsia', 'Gainsboro', 'GhostWhite',
        'Gold',
        'Goldenrod', 'Gray', 'Green', 'GreenYellow', 'Grey', 'Honeydew', 'HotPink', 'IndianRed', 'Indigo', 'Ivory',
        'Khaki',
        'Lavender', 'LavenderBlush', 'LawnGreen', 'LemonChiffon', 'LightBlue', 'LightCoral', 'LightCyan',
        'LightGoldenrodYellow', 'LightGray', 'LightGreen', 'LightGrey', 'LightPink', 'LightSalmon', 'LightSeaGreen',
        'LightSkyBlue', 'LightSlateGray', 'LightSlateGrey', 'LightSteelBlue', 'LightYellow', 'Lime', 'LimeGreen',
        'Linen',
        'Magenta', 'Maroon', 'MediumAquamarine', 'MediumBlue', 'MediumOrchid', 'MediumPurple', 'MediumSeaGreen',
        'MediumSlateBlue', 'MediumSpringGreen', 'MediumTurquoise', 'MediumVioletRed', 'MidnightBlue', 'MintCream',
        'MistyRose', 'Moccasin', 'NavajoWhite', 'Navy', 'OldLace', 'Olive', 'OliveDrab', 'Orange', 'OrangeRed',
        'Orchid',
        'PaleGoldenrod', 'PaleGreen', 'PaleTurquoise', 'PaleVioletRed', 'PapayaWhip', 'PeachPuff', 'Peru', 'Pink',
        'Plum',
        'PowderBlue', 'Purple', 'Rebeccapurple', 'Red', 'RosyBrown', 'RoyalBlue', 'SaddleBrown', 'Salmon', 'SandyBrown',
        'SeaGreen', 'Seashell', 'Sienna', 'Silver', 'SkyBlue', 'SlateBlue', 'SlateGray', 'SlateGrey', 'Snow',
        'SpringGreen',
        'SteelBlue', 'Tan', 'Teal', 'Thistle', 'Tomato', 'Turquoise', 'Violet', 'Wheat', 'White', 'WhiteSmoke',
        'Yellow',
        'YellowGreen')
    headers = {
        "Authorization": "Bearer " + hass_api_token,
        "content-type": "application/json",
    }
    client = discord.Client()

    @client.event
    async def on_ready():
        print('Logged in')
        print("Username: ", end='')
        print(client.user.name)
        print("Userid: ", end='')
        print(client.user.id)

    @client.event
    async def on_message(message):
        if message.author.id == client.user.id:
            return
        if message.content.startswith('!color'):
            url = base_url + "api/states/" + entity_id
            response = requests.get(url, headers=headers)
            res = json.loads(response.text)

            entity = res['state']
            if entity == 'on':
                color = message.content[7:]
                url = base_url + "api/services/light/turn_on"
                if color.lower() in [item.lower() for item in colors]:
                    response = requests.post(url, headers=headers,
                                             json={'entity_id': entity_id, 'transition': '1',
                                                   'color_name': color,
                                                   'brightness_pct': '100'})
                    run = response.text
                    print(message.author.name + ': ' + color)
                    await message.channel.send(
                        ('{0.author.mention} hat die Farbe von '+ entity_name + ' auf ' + color + ' geändert.').format(
                            message))
                else:
                    await message.channel.send(
                        ('{0.author.mention} die Farbe ' + color + ' wird nicht unterstützt.').format(message))
                    await message.channel.send('Lasse dir mit !listcolors die unterstützten Farben auflisten.')
            else:
                await message.channel.send(entity_name + ' ist grade leider aus.')
        elif message.content.startswith('!help'):
            print(message.author.name + ': !help')
            await message.channel.send("Hilfe:\n!color <color> \n!listcolors \n!help")
        elif message.content.startswith('!listcolors'):
            print(message.author.name + ': !listcolors')
            await message.channel.send('Diese Farben werden unterstützt:')
            await message.channel.send(
                'AliceBlue, AntiqueWhite, Aqua, Aquamarine, Azure, Beige, Bisque, Black, BlanchedAlmond, Blue, '
                'BlueViolet, Brown, BurlyWood, CadetBlue, Chartreuse, Chocolate, Coral, CornflowerBlue, Cornsilk, '
                'Crimson, Cyan, DarkBlue, DarkCyan, DarkGoldenrod, DarkGray, DarkGreen, DarkGrey, DarkKhaki, '
                'DarkMagenta, DarkOliveGreen, DarkOrange, DarkOrchid, DarkRed, DarkSalmon, DarkSeaGreen, '
                'DarkSlateBlue, DarkSlateGray, DarkSlateGrey, DarkTurquoise, DarkViolet, DeepPink, DeepSkyBlue, '
                'DimGray, DodgerBlue, FireBrick, FloralWhite, ForestGreen, Fuchsia, Gainsboro, GhostWhite, Gold, '
                'Goldenrod, Gray, Green, GreenYellow, Grey, Honeydew, HotPink, IndianRed, Indigo, Ivory, Khaki, '
                'Lavender, LavenderBlush, LawnGreen, LemonChiffon, LightBlue, LightCoral, LightCyan, '
                'LightGoldenrodYellow, LightGray, LightGreen, LightGrey, LightPink, LightSalmon, LightSeaGreen, '
                'LightSkyBlue, LightSlateGray, LightSlateGrey, LightSteelBlue, LightYellow, Lime, LimeGreen, Linen, '
                'Magenta, Maroon, MediumAquamarine, MediumBlue, MediumOrchid, MediumPurple, MediumSeaGreen, '
                'MediumSlateBlue, MediumSpringGreen, MediumTurquoise, MediumVioletRed, MidnightBlue, MintCream, '
                'MistyRose, Moccasin, NavajoWhite, Navy, OldLace, Olive, OliveDrab, Orange, OrangeRed, Orchid, '
                'PaleGoldenrod, PaleGreen, PaleTurquoise, PaleVioletRed, PapayaWhip, PeachPuff, Peru, Pink, Plum, '
                'PowderBlue, Purple, Rebeccapurple, Red, RosyBrown, RoyalBlue, SaddleBrown, Salmon, SandyBrown, '
                'SeaGreen, Seashell, Sienna, Silver, SkyBlue, SlateBlue, SlateGray, SlateGrey, Snow, SpringGreen, '
                'SteelBlue, Tan, Teal, Thistle, Tomato, Turquoise, Violet, Wheat, White, WhiteSmoke, Yellow, '
                'YellowGreen')
        elif message.content.startswith('!rank'):
            # time.sleep(1)
            print(message.author.name + ': !rank wurde gelöscht')
            await message.delete()

    client.run(auth)

if __name__ == '__main__':
    run_bot(discord_bot_token)
