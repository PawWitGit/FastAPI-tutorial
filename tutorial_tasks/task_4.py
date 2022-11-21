from typing import Union
def inr_to_usd(value:float) -> Union[float, None]:
    try:
        conversion_factor = 75
        value = value/conversion_factor
        return value

    except TypeError:
        return None

print(inr_to_usd("24"))