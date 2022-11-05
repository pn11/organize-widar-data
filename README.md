# Organize WIDAR data

WIDAR のアプリでエクスポートした ZIP ファイルを `zip` ディレクトリに置いて `python orgnize.py` を実行すると、以下を、

```txt
zip/
├── FBX.zip
├── FBX_1.zip
├── FBX_10.zip
├── FBX_11.zip
├── FBX_2.zip
├── FBX_3.zip
├── FBX_8.zip
├── FBX_9.zip
├── GLTF.zip
├── GLTF_1.zip
├── GLTF_2.zip
├── GLTF_3.zip
├── GLTF_4.zip
├── GLTF_5.zip
├── GLTF_6.zip
├── GLTF_7.zip
├── GLTF_8.zip
├── OBJ.zip
├── OBJ_1.zip
├── OBJ_2.zip
├── OBJ_3.zip
├── OBJ_4.zip
├── OBJ_5.zip
├── OBJ_6.zip
├── OBJ_7.zip
├── PLY.zip
├── PLY_1.zip
├── PLY_2.zip
├── PLY_3.zip
├── PLY_4.zip
├── PLY_5.zip
├── PLY_6.zip
├── PLY_7.zip
├── PLY_8.zip
├── STL.zip
├── STL_1.zip
├── STL_2.zip
├── STL_3.zip
├── STL_4.zip
├── STL_5.zip
├── STL_6.zip
└── STL_7.zip
```

以下のように整理する。

```txt
data/
├── 2022-07-28-10-12-24
│   ├── 3Ddata.fbx
│   ├── 3Ddata.glb
│   ├── 3Ddata.mtl
│   ├── 3Ddata.obj
│   ├── 3Ddata.ply
│   ├── 3Ddata.stl
│   └── textures
│       ├── textured_0_v2.jpg
│       └── textured_1_v2.jpg
├── 2022-07-28-22-21-04
│   ├── 3Ddata.fbx
│   ├── 3Ddata.glb
│   ├── 3Ddata.mtl
│   ├── 3Ddata.obj
│   ├── 3Ddata.ply
│   ├── 3Ddata.stl
│   └── textures
│       ├── textured_0_v2.jpg
│       └── textured_1_v2.jpg
├── 2022-08-01-19-04-03
│   ├── 3Ddata.fbx
│   ├── 3Ddata.glb
│   ├── 3Ddata.mtl
│   ├── 3Ddata.obj
│   ├── 3Ddata.ply
│   ├── 3Ddata.stl
│   └── textures
│       └── textured_0_v2.jpg
├── 2022-08-01-19-06-12
│   ├── 3Ddata.fbx
│   ├── 3Ddata.glb
│   ├── 3Ddata.mtl
│   ├── 3Ddata.obj
│   ├── 3Ddata.ply
│   ├── 3Ddata.stl
│   └── textures
│       └── textured_0_v2.jpg
├── 2022-08-01-19-18-20
│   ├── 3Ddata.fbx
│   ├── 3Ddata.glb
│   ├── 3Ddata.mtl
│   ├── 3Ddata.obj
│   ├── 3Ddata.ply
│   ├── 3Ddata.stl
│   └── textures
│       ├── textured_0_v2.jpg
│       └── textured_1_v2.jpg
├── 2022-08-03-20-12-49
│   ├── 3Ddata.fbx
│   ├── 3Ddata.glb
│   ├── 3Ddata.mtl
│   ├── 3Ddata.obj
│   ├── 3Ddata.ply
│   ├── 3Ddata.stl
│   └── textures
│       └── textured_0_v2.jpg
├── 2022-11-05-17-02-32
│   ├── 3Ddata.fbx
│   ├── 3Ddata.glb
│   ├── 3Ddata.mtl
│   ├── 3Ddata.obj
│   ├── 3Ddata.ply
│   ├── 3Ddata.stl
│   └── textures
│       ├── textured_0_v2.jpg
│       └── textured_1_v2.jpg
└── 2022-11-05-17-02-33
    ├── 3Ddata.fbx
    ├── 3Ddata.glb
    ├── 3Ddata.mtl
    ├── 3Ddata.obj
    ├── 3Ddata.ply
    ├── 3Ddata.stl
    └── textures
        ├── textured_0_v2.jpg
        └── textured_1_v2.jpg
```

のように整理する。

