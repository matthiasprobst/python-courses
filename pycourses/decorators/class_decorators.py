import pathlib
import random

from itertools import count

task_id = count()


class _Task:

    def __init__(self, task, name):
        self.id = next(task_id)
        self.task = task
        if name is None:
            name = 'NoName'
        self.name = name

    def __repr__(self):
        return f'<Task {self.name} {self.id}>'

    def __call__(self, *args, **kwargs):
        obj = self.task(*args, **kwargs)
        try:
            _task_method = callable(obj.__getattribute__('task'))
        except AttributeError:
            raise AttributeError(f'Class {self.task.__class__} has no method "task"')
        if not callable(obj.__getattribute__('task')):
            raise TypeError(f'Task seems not to be a method of {self.task.__class__}')
        self.task = obj.task
        return self

    def run(self, *args, **kwargs):
        self.task(*args, **kwargs)


# wrap _Cache to allow for deferred calling
def Task(cls=None):
    def wrapper(function):
        return _Task(function, 'Unknown')

    if cls is None:
        return wrapper

    if not isinstance(cls, str):
        return _Task(cls, None)
    else:
        name = 'NoName'
        return wrapper


@Task('task1')
class MyTask:

    def __init__(self, simulation_filename: pathlib.Path):
        self.simulation_filename = simulation_filename

    def task(self, flag, input_data, **kwargs):
        """simulate a simulation. A random variable decides if simulation fails or not"""

        if self.simulation_filename is None:
            raise ValueError('Got no simulation filename')

        verbose = kwargs.get('verbose', False)
        if verbose:
            print(f'filename: {self.simulation_filename}')

        if 'result' in input_data:
            if not flag:
                input_data['result'] = 0
            if random.random() < 0.5:
                # make simulation fail
                if verbose:
                    print('Simulation failed')
                return False, {'result': input_data['result']}
            if verbose:
                print('Simulation succeeded')
            return True, {'result': input_data['result'] + 1}
        if random.random() < 0.5:
            # make simulation fail
            if verbose:
                print('Simulation failed')
            return False, {'result': 0}
        if verbose:
            print('Simulation succeeded')
        return True, {'result': 1}


t = MyTask('hallo')
t.run(0, {'yo': 'no'}, verbose=True)
print(t)
