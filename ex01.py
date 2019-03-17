for i in range(10):
    print('{} Hello World!'.format(i))

class Sample_Object:
    pass

if __name__ == "__main__":
    sample_object = Sample_Object()
    print(sample_object.__dir__())