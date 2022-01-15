"""Config module."""
import yaml


def get_config():
    """Load config from config.yaml file."""
    stream = open('config.yaml', 'r')
    try:
        return yaml.safe_load(stream)
    except yaml.YAMLError:
        raise ValueError(
            'Something goes wrong with you config file. Please check config.yaml file.'
        )

settings = get_config()

plants_type = {
    'lemon': '//*[@id="crafting-items"]/div[1]/div/img[2]',
    'orange': '//*[@id="crafting-items"]/div[2]/div/img[2]',
    'pear': '//*[@id="crafting-items"]/div[3]/div/img[2]',
    'watermelon': '//*[@id="crafting-items"]/div[4]/div/img[2]',
    'pineapple': '//*[@id="crafting-items"]/div[5]/div/img[2]',
    'apple': '//*[@id="crafting-items"]/div[6]/div/img[2]',
}
