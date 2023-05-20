import struct

def convert_obj_to_trk(obj_file_path, trk_file_path):
    # Read the OBJ file
    with open(obj_file_path, 'r') as obj_file:
        vertices = []
        faces = []
        for line in obj_file:
            if line.startswith('v '):
                _, x, y, z = line.split()
                vertices.append((float(x), float(y), float(z)))
            elif line.startswith('f '):
                _, v1, v2, v3 = line.split()
                faces.append((int(v1.split('/')[0]), int(v2.split('/')[0]), int(v3.split('/')[0])))

    # Write the TRK file
    with open(trk_file_path, 'wb') as trk_file:
        # Write header
        trk_file.write(struct.pack('<H', 100))  # Arbitrary header value
        trk_file.write(struct.pack('<B', 1))  # Number of objects

        # Write object data
        trk_file.write(struct.pack('<B', 1))  # Object type (1 = mesh)
        trk_file.write(struct.pack('<H', len(vertices)))  # Number of vertices

        for vertex in vertices:
            trk_file.write(struct.pack('<fff', *vertex))

        trk_file.write(struct.pack('<H', len(faces)))  # Number of faces

        for face in faces:
            trk_file.write(struct.pack('<HHH', *face))

        print("conversion completed succesfully :)")

# Example usage
obj_file_path = 'input.obj'
trk_file_path = 'output.trk'
convert_obj_to_trk(obj_file_path, trk_file_path)
