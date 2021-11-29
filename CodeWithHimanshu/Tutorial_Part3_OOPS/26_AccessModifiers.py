class Access:
    public_variable_named_as_it_is = 1
    _protected_variable_named_with_underscore_prefix = 2
    __private_variable_named_with_double_underscore_prefix = 3


class Derived(Access):
    var_prot = Access._protected_variable_named_with_underscore_prefix
    var_pub = Access.public_variable_named_as_it_is
    # var_priv = Access.__priv...  # cannot access the private var outsite Access
    pass


class Derived2:
    var_pub = Access.public_variable_named_as_it_is  # only public variable of Access is accessible
    # var_prot = Access.__prot...    # cannot access the protected var since the class is  not an instance of Access


one = Access()
print(one.public_variable_named_as_it_is)  # public variable
derived = Derived()
print(derived.var_prot)
derived2 = Derived2()
print(derived2.var_pub)


# Name Mengling: To access private variable we need to follow a format: obj._ClassName__privVarName
print(one._Access__private_variable_named_with_double_underscore_prefix)

