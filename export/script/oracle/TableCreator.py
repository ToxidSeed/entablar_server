class TableCreator:
    def __init__(self):
        self.drop_table = False
        self.table_name = ''
        self.fields = {}
        pass

    def create_table(self):
        # sentence
        create_table_str = 'CREATE TABLE {} (\n{}\n);'.format(self.table_name, self.fields_to_str())
        file_name = '{}.sql'.format(self.table_name)
        file_path = './output/'
        file = '{}{}'.format(file_path, file_name)
        TableCreator.save_script(file, create_table_str)
        file_info = {
            "file_name":file_name,
            "file":file
        }
        return file_info

    @staticmethod
    def save_script(file, script=''):
        file_object = open(file, "w")
        file_object.write(script)

    def fields_to_str(self):
        fields_list = []
        for item in self.fields:
            field_stmt = '{} {}'.format(item['nombre'], item['tipo_dato_text'])
            fields_list.append(field_stmt)

        fields_str = ',\n'.join(fields_list)
        return fields_str

