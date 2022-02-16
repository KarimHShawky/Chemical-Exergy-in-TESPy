import CoolProp.CoolProp as CP

# print all alias of a given fluid
print(CP.get_fluid_param_string('ethane', 'aliases'))

# print CoolProp fluids list
print(CP.FluidsList())

# iterate Coolprop fluids list and print alias
for i in CP.FluidsList():
    print(i)
    print(CP.get_fluid_param_string(i, 'aliases'))

