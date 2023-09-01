import ee
# ee.Authenticate()
# ee.Initialize()

service_account = 'brian-python@ee-briansimiyu.iam.gserviceaccount.com'
credentials = ee.ServiceAccountCredentials(service_account, './ee-brianchelloti-f3bf0b9227be.json')
ee.Initialize(credentials)


####################### Shoreline Analysis Parameters #################

# 1. Define the area of interest
'''Note: always change from null to None, and false to False'''
aoi =  ee.Geometry.Polygon(
        [[[57.216958051410614, -20.481426350274322],
          [57.3193122394282, -20.51941679337143],
          [57.522902632494606, -20.12696025857025],
          [57.38626017643992, -20.105683257847108]]], None, False);



# geometry = ee.Geometry.Polygon(
#         [[[57.36779186042595, -20.32139946609873],
#           [57.39079448493767, -20.308198784877142],
#           [57.40178081306267, -20.220595058286616],
#           [57.36744853767205, -20.219306399445856],
#           [57.351999013746266, -20.325262867088504]]], None, False),
# geometry2 = ee.Geometry.Polygon(
#         [[[57.44400951179314, -20.163561697120315],
#           [57.416200368726734, -20.175485650871128],
#           [57.38942119392205, -20.202875063681432],
#           [57.376718252027516, -20.22381665868126],
#           [57.395944326246266, -20.22736034204],
#           [57.46529552253533, -20.174518877769984],
#           [57.46117564948845, -20.15904969316843]]], None, False),
# geometry3 = ee.Geometry.Polygon(
#         [[[57.36153912031839, -20.31283182142665],
#           [57.3344166227598, -20.45250444351781],
#           [57.38076519453714, -20.461832892831307],
#           [57.40190176138199, -20.303634512473415],
#           [57.362419644682774, -20.304600482627247]]], None, False);

# aoi = [geometry, geometry2, geometry3]
# aoi = aoi[0]
# for i in range(len(aoi)):
#     print(i)
    
# aoiList = []
# for i range(len(aoi)):
#     aoi = 

# aoi = ee.Geometry.Polygon(
#         [[[73.40292280861833, -0.27289197693677386],
#           [73.40292280861833, -0.3190682699554407],
#           [73.4454948301027, -0.3190682699554407],
#           [73.4454948301027, -0.27289197693677386]]], None, False);

# 2. Define start date and end date
date = ['2016-01-01', '2016-12-31']

# 3. Georeferencing
horizontal_step = 0     # (+ Positive) Move to right // (- Negative) Move to left
vertical_step = 0       # (+ Positive) Move to top // (- Negative) Move to bottom

########################################################################