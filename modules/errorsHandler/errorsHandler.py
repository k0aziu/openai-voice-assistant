class errorsHandler:
    def __init__(self, error_code, error_message):
        self.error_name = error_code
        self.error_message = error_message

    errors = {
        'system_not_recognized': 'Nie rozpoznano systemu.',
        'not_found': 'Nie znaleziono zasobu.'
    }

    def handle_error(self):
        for error in self.errors:
            if error == self.error_name:
                return self.errors[error]
            else:
                return "Wystąpił nieznany błąd."
