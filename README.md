# awsebdirect
Wrapper around the AWS elastic beanstalk for easy access to useful and more used functions.

## Usage

Without installing:
```
python3 ebd.py count
```
Them will count the available environments, showing the count in each region.

```
python3 ebd.py count_apps
```
Them will count the number of available applications (still not working)

```
python3 ebd.py infos
```
May display informations from each environment, as region, containing application and instance size.
