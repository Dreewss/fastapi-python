from pydantic import BaseModel
import json
from typing import List, Dict

class JsonDB(BaseModel):
    path: str

    def read(self) -> List[Dict]:
        try:
            with open(self.path, 'r') as f:
                data = json.load(f)
            if isinstance(data, list):
                return data
            return []
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def insert(self, product: Dict):
        data = self.read()
        data.append(product)
        with open(self.path, 'w') as f:
            json.dump(data, f, indent=4)
