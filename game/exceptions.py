class InvalidRollError(Exception):
    def __str__(self):
        return "Бросок не сделан!!! Нажмите 'Enter' для повторного броска."