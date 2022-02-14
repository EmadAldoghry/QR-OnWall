import ifcopenshell
import qrcode

ifc_path = '.\BIM_Building_Model.ifc'

m = ifcopenshell.open(ifc_path)
walls = m.by_type('IfcWall')

Wall_guid = []  
for wall in walls:
    Wall_info = wall.get_info()
    Wall_id =  Wall_info['id']
    data = Wall_info['GlobalId']
    Wall_guid.append(data)
    filename = (f"wall_{Wall_id}.png")
    img = qrcode.make(data)
    img.save(filename)

