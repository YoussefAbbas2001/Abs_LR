# Abs_LR
This is a implementaiton for LR in pytorch for testing different tools

# PROJECT ORGANIZATION
pytorch-project/
> README.md </br>
> config.py</br>
> train.py</br>
> test.py</br>
> evaluate.py</br>
> models/</br>
>> __init__.py</br>
>> model.py</br>
>> cnn/</br>
>>> __init__.py</br>
>>> cnn.py</br>
>>> resnet.py</br>

>> rnn/</br>
>>> __init__.py</br>
>>> rnn.py</br>
>>> lstm.py</br>
 
> data/            </br>
>> __init__.py     </br>
>> data.py</br>
>> dataset.py</br>
>> dataloader.py</br>
>> transforms.py</br>

> losses/                  </br>
>> __init__.py</br>
>> loss.py</br>
>> cross_entropy.py</br>

> metrics/          </br>
>> __init__.py</br>
>> metric.py</br>
>> accuracy.py</br>

> optimizers/     </br>
>> __init__.py</br>
>> optimizer.py</br>
>> adam.py</br>

> utils/           </br>
>> __init__.py</br>
>> logger.py</br>
>> timer.py</br>
>> plotter.py</br>

> results/           </br>
>> model.pth</br>
>> predictions.csv</br>
>> plots/</br>
>>> loss.png</br>
>>> accuracy.png</br>

> logs/        </br>
>> train.log</br>
>> test.log</br>

# REFERENCES
* [Simple Linear Regression in Pytoch](https://towardsdatascience.com/linear-regression-with-pytorch-eb6dedead817)
* [Project Organization](https://www.geeksforgeeks.org/how-to-structure-a-pytorch-project/)