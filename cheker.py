

def duck_filter(native, ember_goose, reference, base_distinction, special_destinction): # a - native, b - ember_goose, c - reference
    
    import random
    from scipy import stats
    from numpy import std, mean, sqrt
    
    def cohen_d(x,y):
        nx = len(x)
        ny = len(y)
        dof = nx + ny - 2
        return (mean(x) - mean(y)) / sqrt(((nx-1)*std(x, ddof=1) ** 2 + (ny-1)*std(y, ddof=1) ** 2) / dof)
    
    
    for pos in native: # для каждой позиции в нативном фаге

        if reference[pos-3:pos+4] in ember_goose: # если этот ключ есть в библиотеке от эмбер

            print('{} from {}'.format(pos, len(reference)), end = '')

            if len(ember_goose[reference[pos-3:pos+4]]) < 300 or len(native[pos]) < 300: # проверка на наш нижний фильтр  

                del base_distinction[pos]  # тут вставить предсказателя
                del special_destinction[pos]

                continue

            else: 

                if len(native[pos]) > 1000: 
                    native[pos] = random.sample(native[pos], 1000)

                if len(ember_goose[reference[pos-3:pos+4]]) > 1000: 
                    ember_goose[reference[pos-3:pos+4]] = random.sample(ember_goose[reference[pos-3:pos+4]], 1000)


                test_ks = stats.ks_2samp(native[pos] ,ember_goose[reference[pos-3:pos+4]])
                base_distinction[pos][0] = reference[pos-3:pos+4]
                base_distinction[pos][1] = test_ks[1]

                effect_size = cohen_d(native[pos], ember_goose[reference[pos-3:pos+4]]) 
                base_distinction[pos][2] = effect_size

                if test_ks[1] < 1e-30 and abs(effect_size) > 0.25 : # effect size - по модулю

                    special_destinction[pos][0] = reference[pos-3:pos+4]
                    special_destinction[pos][1] = test_ks[1]
                    special_destinction[pos][2] = effect_size

                else: del special_destinction[pos]


            print('\r', end = '')

        else: 
            del base_distinction[pos]
            del special_destinction[pos]