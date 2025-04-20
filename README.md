# Decorator Logging Library #

## What is this? ##
The module allows you to wrap function with a logger (based on loguru) and specify some additional options (log level, log timing)

----------

### Using ###



    class Roles:
        def __init__(self, file_name: str):
            self.file_name = file_name
            self.roles = self.read()
    
        @SyncLoggable()
        def add_role(self, user_id: int, role: Role) -> None:
            user_roles = self.roles.get(user_id, [])
            user_roles.append(role)
            self.roles[user_id] = user_roles
            self.save()
    
        def save(self) -> None:
            ...
    
        def read(self) -> dict[int, list[Role]]:
            ...

example output for add_role(123, Role.ADMIN):

INFO: Executing add_role with args: \['123', 'Role.ADMIN'\]}

INFO: Success add_role returned: None

----------


## Developer ##
GitHub: [link](https://github.com/ArgentumX/) 
