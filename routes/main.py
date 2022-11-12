from fastapi import Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import datetime as dt
from fastapi import APIRouter
from starlette.responses import RedirectResponse
from pyModbusTCP.client import ModbusClient
import pathlib
import json
c = ModbusClient(host="localhost", port=502, unit_id=1,
                 auto_open=False, auto_close=False)
web = APIRouter()
templates = Jinja2Templates(directory='templates')
greq = ''
data = {}
setupList = []
key_list = ['workmode', 'maxSellPower', 'solarSell', 'timeOfUse', 'hour1', 'power1', 'soc1', 'mode1',
            'hour2', 'power2', 'soc2', 'mode2', 'hour3', 'power3', 'soc3', 'mode3', 'hour4', 'power4', 'soc4',
            'mode4', 'hour5', 'power5', 'soc5', 'mode5', 'hour6', 'power6', 'soc6', 'mode6', 'maxSolarPower', 'pattern']
value_list = [0, 0, 0, 0, 123, 0, 0, 0, 1000, 0, 0,
              0, 1000, 0, 0, 0, 1000, 0, 0, 0, 1000, 0, 0, 0, 1000, 0, 0, 0, 0, 0]


def convertBool(data: str):
    if data == 'on':
        return '1'
    else:
        return '0'


def convertWorkMode(data: str):
    if data == 'With panel pv':
        return 1
    else:
        return 0


def convertStringHour(data: str):
    return int(data.replace(':', ''))


def jsonUpdate():
    with open(str(pathlib.Path().absolute())+'\static\js\data.json', "w") as outfile:
        outfile.write(json.dumps(data))


@web.on_event('startup')
async def startup():
    pass


@web.get('/', response_class=HTMLResponse)
async def main():
    response = RedirectResponse(url=f"/index/i", status_code=302)
    return response


@web.get('/prueba/')
async def lim(request: Request):
    context = {'request': request}
    return templates.TemplateResponse('probar.html', context=context)


@web.get('/limgrid/{req}')
async def lim(request: Request, req: str):
    global greq
    context = {'request': request, "req": req}
    greq = req
    return templates.TemplateResponse('limgridlim.html', context=context)


@web.get('/confall/{wk}')
async def confallG(request: Request, wk: int):
    global data
    data.update({'workmode': wk})
    if wk == 'Without panel pv':
        data.update({'solarSell': 0, 'maxSolarPower': 0})
    context = {'request': request, 'req': greq}
    return templates.TemplateResponse('confall.html', context=context)


@web.get('/tou')
async def configtouG(request: Request):
    context = {'request': request, 'req': greq}
    return templates.TemplateResponse('tou.html', context=context)


@web.get('/conftime')
async def config(request: Request):
    context = {'request': request, 'req': greq}
    return templates.TemplateResponse('conftime.html', context=context)


@web.post('/tou')
async def configtouP(timeOfUse: str = Form('off'), monday: str = Form('off'), tuesday: str = Form('off'),
                     wednesday: str = Form('off'), thursday: str = Form('off'), friday: str = Form('off'),
                     saturday: str = Form('off'), sunday: str = Form('off'), mode1: str = Form(...),
                     mode2: str = Form(...), mode3: str = Form(...), mode4: str = Form(...), mode5: str = Form(...), mode6: str = Form(...)):
    global data
    data.update({'timeOfUse': int(convertBool(timeOfUse) + convertBool(monday) + convertBool(tuesday) + convertBool(
        wednesday)+convertBool(thursday)+convertBool(friday)+convertBool(saturday) + convertBool(sunday), 2), 'mode1': int(mode1), 'mode2': int(mode2), 'mode3': int(mode3), 'mode4': int(mode4), 'mode5': int(mode5), 'mode6': int(mode6)})
    response = RedirectResponse(url=f"/tou", status_code=302)

    list_out = list(data.values())
    c.open()
    if c.write_multiple_registers(0, list_out):
        print("write ok")
    else:
        print("write error")
    c.close()
    response = RedirectResponse(url=f"/tou", status_code=302)
    return response


@web.post('/confall')
async def configallP(solarSell: str = Form('off'), pattern: str = Form(...), maxSellPower: str = Form(...), maxSolarPower: str = Form('0')):
    global data
    data.update({"solarSell": int(convertBool(solarSell)), 'pattern': int(pattern),
                'maxSellPower': int(maxSellPower), 'maxSolarPower': int(maxSolarPower)})
    response = RedirectResponse(url=f"/tou", status_code=302)
    return response


@web.post('/conftime1')
async def conftimeP1(hour1: str = Form(0), power1: str = Form(0), soc1: str = Form(0), hour2: str = Form(0),
                     power2: str = Form(0), soc2: str = Form(0), hour3: str = Form(0), power3: str = Form(0),
                     soc3: str = Form(0), hour4: str = Form(0), power4: str = Form(0), soc4: str = Form(0),
                     hour5: str = Form(0), power5: str = Form(0), soc5: str = Form(0), hour6: str = Form(0),
                     power6: str = Form(0), soc6: str = Form(0)):
    global data
    data.update({'hour1': convertStringHour(hour1),
                'power1': int(power1), 'soc1': int(soc1), 'hour2': convertStringHour(hour2),
                 'power2': int(power2), 'soc2': int(soc2), 'hour3': convertStringHour(hour3),
                 'power3': int(power3), 'soc3': int(soc3), 'hour4': convertStringHour(hour4),
                 'power4': int(power4), 'soc4': int(soc4), 'hour5': convertStringHour(hour5),
                 'power5': int(power5), 'soc5': int(soc5), 'hour6': convertStringHour(hour6),
                 'power6': int(power6), 'soc6': int(soc6)})
    response = RedirectResponse(url=f"/conftime", status_code=302)
    jsonUpdate()
    return response


@web.post('/settings/{name}/{description}')
async def setting(name: str = 'pa', description: str = 'pa', timeOfUse: str = Form('off'), monday: str = Form('off'), tuesday: str = Form('off'),
                  wednesday: str = Form('off'), thursday: str = Form('off'), friday: str = Form('off'),
                  saturday: str = Form('off'), sunday: str = Form('off'), mode1: str = Form(...),
                  mode2: str = Form(...), mode3: str = Form(...), mode4: str = Form(...), mode5: str = Form(...), mode6: str = Form(...)):
    global setupList, data
    data.update({'timeOfUse': int(convertBool(timeOfUse) + convertBool(monday) + convertBool(tuesday) + convertBool(
        wednesday)+convertBool(thursday)+convertBool(friday)+convertBool(saturday) + convertBool(sunday), 2),
        'mode1': int(mode1), 'mode2': int(mode2), 'mode3': int(mode3), 'mode4': int(mode4), 'mode5': int(mode5), 'mode6': int(mode6)})
    setupList.append({'name': name, 'description': description, 'data': data})
    with open(str(pathlib.Path().absolute())+'\static\js\configs.json', "r") as infile:
        configs = json.load(infile)
    configs.append({'name': name, 'description': description, 'data': data})
    with open(str(pathlib.Path().absolute())+'\static\js\configs.json', "w") as outfile:
        outfile.write(json.dumps(configs))
    response = RedirectResponse(url=f"/conftime", status_code=302)
    jsonUpdate()
    return response


@web.get('/delete/{name}')
async def edit(name: str):
    global setupList
    with open(str(pathlib.Path().absolute())+'\static\js\configs.json', "r") as infile:
        configs = json.load(infile)
    for config in configs:
        if config['name'] == name:
            configs.remove(config)
            break
    with open(str(pathlib.Path().absolute())+'\static\js\configs.json', "w") as outfile:
        outfile.write(json.dumps(configs))
    message = '0'
    response = RedirectResponse(url=f"/index/{message}", status_code=302)
    return response


@web.get('/activate/{name}')
async def edit(name: str):
    global setupList
    with open(str(pathlib.Path().absolute())+'\static\js\configs.json', "r") as infile:
        configs = json.load(infile)
    for config in configs:
        if config['name'] == name:
            list_out = list(config['data'].values())
            c.open()
            if c.write_multiple_registers(0, list_out):
                print("write ok")
            else:
                print("write error")
            c.close()
            break
    message = '1'
    response = RedirectResponse(url=f"/index/{message}", status_code=302)
    return response


def int2Hour(num: int):
    if len(str(num)) == 4:
        hour = str(num)[0:2]
        minutes = str(num)[2:4]
        return hour + ":" + minutes
    else:
        hour = str(num)[0:1]
        minutes = str(num)[1:3]
        return '0' + hour + ":" + minutes


def num2binary(x):
    lista = ''
    for i in range(1, 9):
        try:
            lista += (x[-i])
        except:
            lista += ('0')
    return lista


def modes(entry):
    if entry == 0:
        return 'No charge'
    elif entry == 1:
        return 'Grid charge'
    elif entry == 2:
        return 'Generator charge'
    elif entry == 3:
        return 'Grid or gencharging'


@web.get('/show/{name}')
async def show(request: Request, name: str):
    with open(str(pathlib.Path().absolute())+'\static\js\configs.json', "r") as infile:
        configs = json.load(infile)
    for config in configs:
        if config['name'] == name:
            list_out = config['data']
            break
    if list_out['workmode'] == 0:
        list_out['workmode'] = 'Limited power to load'
    elif list_out['workmode'] == 1:
        list_out['workmode'] = 'Grid selling'
    elif list_out['workmode'] == 2:
        list_out['workmode'] = 'Limited to home'

    timeofuse = num2binary(bin(list_out['timeOfUse'])[2:])
    list_out['timeOfUse'] = timeofuse[0]
    list_out['monday'] = timeofuse[1]
    list_out['tuesday'] = timeofuse[2]
    list_out['wednesday'] = timeofuse[3]
    list_out['thursday'] = timeofuse[4]
    list_out['friday'] = timeofuse[5]
    list_out['saturday'] = timeofuse[6]
    list_out['sunday'] = timeofuse[7]
    list_out['hour1'] = int2Hour(list_out['hour1'])
    list_out['hour2'] = int2Hour(list_out['hour2'])
    list_out['hour3'] = int2Hour(list_out['hour3'])
    list_out['hour4'] = int2Hour(list_out['hour4'])
    list_out['hour5'] = int2Hour(list_out['hour5'])
    list_out['hour6'] = int2Hour(list_out['hour6'])
    list_out['pattern'] = 'Load first' if list_out['pattern'] == 0 else 'Battery first'
    list_out['mode1'] = modes(list_out['mode1'])
    list_out['mode2'] = modes(list_out['mode2'])
    list_out['mode3'] = modes(list_out['mode3'])
    list_out['mode4'] = modes(list_out['mode4'])
    list_out['mode5'] = modes(list_out['mode5'])
    list_out['mode6'] = modes(list_out['mode6'])
    context = {'request': request, 'data': list_out}
    response = templates.TemplateResponse('show.html', context=context)
    return response


@ web.get('/index/{ms}', response_class=HTMLResponse)
async def main(request: Request, ms: str = ''):
    global value_list, data
    c.open()
    regs = c.read_holding_registers(0, 30)
    if regs:
        value_list = regs
        data = dict(zip(key_list, value_list))
        jsonUpdate()
    else:
        data = dict(zip(key_list, value_list))
        jsonUpdate()
    c.close()
    with open(str(pathlib.Path().absolute())+'\static\js\configs.json', "r") as infile:
        configs = json.load(infile)
    for i in configs:
        if i['data'] == data:
            configs[configs.index(i)]['active'] = 1
        else:
            configs[configs.index(i)]['active'] = 0
    context = {'request': request, 'configs': configs, 'message': ms}
    return templates.TemplateResponse('index.html', context=context)
