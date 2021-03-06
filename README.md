# click-tracker-mvp

## About
This is a simple MVP for a click tracking application.

The main datastore here is an in-memory python Dictionary that uses a datetime representation for Keys and a list of (userid, event) tuples as a values.

Key is converted from a time since epoch to a representation using YYYYMMDDHH.

Example:
key: 2017030205, value: [('testuser','click'), ('testuser', 'impression'),('testuser2','click')]

This allows consumers to GET an hour block of a given Year, Month, Day.

## API
API has two endpoints:
```
POST /analytics?timestamp={millis_since_epoch}&user={user_id}&event={click|impression}
GET /analytics?timestamp={millis_since_epoch}
```
POST returns a 204 unless there's an issue.
GET returns a JSON blob containing:
```
{
  "clicks": x,
  "impressions": y 
  "unique_user": z
}
```

## INSTALLATION

#### Recommended
Install using virtualenv.
```
> git clone https://github.com/jonmoshier/click-tracker-mvp
> cd click-tracker-mvp
click-tracker-mvp> virtualenv virt
click-tracker-mvp> source virt/bin/activate
(virt) click-tracker-mvp> pip install -r requirements.txt
(virt) click-tracker-mvp> python api.py
```

#### Custom

You just need to install Flask using
```
> pip install flask
```
or 
```
pip install -r requirements.txt
```

This is just an experiment and isn't intended to be anything but an execise.
