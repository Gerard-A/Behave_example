from behave import given, when, then, step
from hamcrest import assert_that, equal_to, has_item
from features.resources.location_resource import LocationResource


@given("the country code '{country_code}' and zip code '{zip_code}'")
def country_code_and_zip_code(context, country_code, zip_code):
    context.resource = LocationResource(country_code, zip_code)


@when("I request the locations corresponding to these codes")
def request_locations(context):
    context.response = context.resource.send_request()


@then("the response contains the place name '{place_name}'")
def response_contains_place_name(context, place_name):
    places = []
    for index in range(len(context.response.json()['places'])):
        places.append(context.response.json()['places'][index]['place name'])
    assert_that(places, has_item(place_name))


@then("the response contains the state '{state_name}'")
def response_contains_state(context, state_name):
    assert_that(context.response.json()['places'][0]['state'], equal_to(state_name))


@then("the response contains exactly '{nr_of_locations}' location")
def response_contains_1_location(context, nr_of_locations):
    response_contains_nr_of_locations(context, nr_of_locations)


@then("the response contains exactly '{nr_of_locations}' locations")
def response_contains_nr_of_locations(context, nr_of_locations):
    assert_that(len(context.response.json()['places']), equal_to(int(nr_of_locations)))


@then("the response has status code '{status_code}'")
def response_has_status_code(context, status_code):
    assert_that(context.response.status_code, equal_to(int(status_code)))
