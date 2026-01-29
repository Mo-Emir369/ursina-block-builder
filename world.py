from ursina import Entity, scene, destroy, Vec3
from blocks import BLOCKS

class Block(Entity):
    def __init__(self, pos, block_type: str):
        data = BLOCKS[block_type]
        super().__init__(
            model="cube",
            texture=data["texture"],
            color=data["tint"],
            position=Vec3(*pos),
            parent=scene,
            origin_y=0.5,
            collider="box",
        )
        self.block_type = block_type


class World:
    def __init__(self):
        # key: "x,y,z" -> Block entity
        self.blocks = {}

    @staticmethod
    def to_grid_pos(pos) -> Vec3:
        """Accept tuple/list/Vec3 and snap to integer grid."""
        if isinstance(pos, (tuple, list)):
            x, y, z = pos
            return Vec3(int(x), int(y), int(z))
        # Vec3 or any object with x,y,z
        return Vec3(int(pos.x), int(pos.y), int(pos.z))

    @classmethod
    def key_from_pos(cls, pos) -> str:
        p = cls.to_grid_pos(pos)
        return f"{int(p.x)},{int(p.y)},{int(p.z)}"

    @staticmethod
    def tuple_from_key(k: str):
        x, y, z = k.split(",")
        return (int(x), int(y), int(z))

    def has(self, pos) -> bool:
        return self.key_from_pos(pos) in self.blocks

    def add_block(self, pos, block_type: str) -> bool:
        k = self.key_from_pos(pos)
        if k in self.blocks:
            return False
        b = Block(self.tuple_from_key(k), block_type)
        self.blocks[k] = b
        return True

    def remove_block(self, pos) -> bool:
        k = self.key_from_pos(pos)
        if k not in self.blocks:
            return False
        destroy(self.blocks[k])
        del self.blocks[k]
        return True

    def to_save_data(self) -> dict:
        return {k: self.blocks[k].block_type for k in self.blocks}

    def load_from_data(self, data: dict):
        for k in list(self.blocks.keys()):
            destroy(self.blocks[k])
            del self.blocks[k]

        for k, t in data.items():
            self.add_block(self.tuple_from_key(k), t)
