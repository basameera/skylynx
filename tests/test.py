import setup_path
import skylynx
import skylynx.utils as su


if __name__ == "__main__":
    print('skylynx', skylynx.__version__)

    # JSON
    # Write
    data_dict = dict(
        a=123,
        b='skylynx'
    )
    su.json_write('misc/example.json', data_dict)

    # Read
    data = su.json_read('misc/example.json')
    print(data)

    # YAML
    # Write
    su.yaml_write('misc/example.yaml', data_dict)

    # Read
    data = su.yaml_read('misc/example.yaml')
    print(data)
