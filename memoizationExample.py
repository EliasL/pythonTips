import json
import time
from pathlib import Path
import hashlib
from numpy import asarray


def slow_sum(data):
    time.sleep(2)
    return sum(data)


def getUniqueName(data):
    data_bytes = asarray(data).tobytes()
    h = hashlib.sha1()
    h.update(data_bytes)
    name = h.hexdigest()
    return name


def fast_sum(data):
    # Check if we have the answer already
    dataPath = Path(".sumData")
    dataPath.mkdir(exist_ok=True)
    filePath = dataPath / getUniqueName(data)

    if filePath.exists():
        # load file
        with open(filePath, "r") as f:
            data = json.load(f)
            return data["result"]
    else:
        # This takes a long time
        result = slow_sum(data)

        # Save results
        with open(filePath, "w") as f:
            json.dump({"result": result}, f)
        return result


if __name__ == "__main__":
    #print(slow_sum(range(50)))
    print(fast_sum(range(50)))
