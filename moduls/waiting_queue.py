class Descriptor:
    __slots__ = 'name'

    def __set_name__(self, owner, name):
        self.name = f'_{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        match self.name:
            case '_standby_count':
                if value < 0:
                    raise ValueError('_standby_count cannot be less than zero.')
            case '_persons_count':
                if getattr(instance, '_standby_count') > value:
                    raise ValueError('_persons_count cannot be less than _standby_count.')
            case '_wait_point_km':
                if value < 1:
                    raise ValueError('_wait_point_km cannot be less than one.')
            case '_end_point_km':
                if value < 2:
                    raise ValueError('_wait_point_km cannot be less than two.')

                if getattr(instance, '_wait_point_km') > value:
                    raise ValueError('_end_point_km cannot be less than _wait_point_km.')

        setattr(instance, self.name, value)


class WaitingQueue:
    __slots__ = ('_persons_count', '_standby_count', '_wait_point_km', '_end_point_km', '_step_wait_point_km')

    persons_count = Descriptor()
    standby_count = Descriptor()
    wait_point_km = Descriptor()
    step_wait_point_km = Descriptor()
    end_point_km = Descriptor()

    def __init__(self, persons_count=3, wait_point_km=500, end_point_km=5000):
        self.standby_count = 0 
        self.persons_count = persons_count
        self.wait_point_km = wait_point_km
        self.step_wait_point_km = self.wait_point_km
        self.end_point_km = end_point_km

    def __repr__(self):
        return f'standby_count: {self.standby_count} ' \
               f'persons_count: {self.persons_count} ' \
               f'wait_point_km: {self.wait_point_km} ' \
               f'end_point_km: {self.end_point_km}'


if __name__ == '__main__':
    print(WaitingQueue())
