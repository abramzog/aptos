from termcolor import colored


class Formatter:

    @staticmethod
    def format_successful_action(for_message):
        return colored('success', 'green') + ' {!r}'.format(for_message)

    @staticmethod
    def format_unsuccessful_action(for_message):
        return colored('error', 'red') + ' {!r}'.format(for_message)

    @staticmethod
    def valid_instance_meesage(instance, schema):
        return ' instance {!r} is valid against the schema {!r}'.format(instance, schema)

    @staticmethod
    def cannot_convert_schema_message(schema, format):
        return ' cannot convert schema {!r} into {!r} format, schema must be of type "object"'.format(schema,
                                                                                                      format)
