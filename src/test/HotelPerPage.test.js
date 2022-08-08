import {HotelPerPage} from "../components/HotelPerPage.js";
import fetch from 'cross-fetch';
import TestingHotelDetails from './../TestingHotelDetails';
test('Empty Hotel Slicing test',async()=>{
    const test_props = [];
    const res = await HotelPerPage(test_props).then();
    expect(res).toEqual([]);
})

test('Non-empty Hotel Slicing test',async()=>{
    const test_hotelList = [{"id":"lXJq","searchRank":0.79,"price_type":"multi","max_cash_payment":53.86,"coverted_max_cash_payment":75.72,"points":1875,"bonuses":0,"lowest_price":53.86,"price":75.72,"converted_price":75.72,"lowest_converted_price":75.72,"market_rates":[{"supplier":"expedia","rate":75.722307214}]},{"id":"iRm9","searchRank":0.91,"price_type":"multi","max_cash_payment":480.65,"coverted_max_cash_payment":675.75,"points":16875,"bonuses":0,"lowest_price":480.65,"price":675.75,"converted_price":675.75,"lowest_converted_price":675.75,"market_rates":[{"supplier":"expedia","rate":611.880106678}]},{"id":"dXFm","searchRank":0.75,"price_type":"multi","max_cash_payment":63.91,"coverted_max_cash_payment":89.85,"points":2225,"bonuses":0,"lowest_price":63.91,"price":89.85,"converted_price":89.85,"lowest_converted_price":89.85,"market_rates":[{"supplier":"expedia","rate":89.851701709}]},{"id":"NhJ1","searchRank":0.94,"price_type":"multi","max_cash_payment":57.4,"coverted_max_cash_payment":80.7,"points":2000,"bonuses":0,"lowest_price":57.4,"price":80.7,"converted_price":80.7,"lowest_converted_price":80.7,"market_rates":[{"supplier":"expedia","rate":70.281435901}]},{"id":"nPbT","searchRank":2,"price_type":"multi","max_cash_payment":254.59,"coverted_max_cash_payment":357.93,"points":8925,"bonuses":0,"lowest_price":254.59,"price":357.93,"converted_price":357.93,"lowest_converted_price":357.93,"market_rates":[]},{"id":"qO6Y","searchRank":0.69,"price_type":"multi","max_cash_payment":324.52,"coverted_max_cash_payment":456.25,"points":11400,"bonuses":0,"lowest_price":324.52,"price":456.25,"converted_price":456.25,"lowest_converted_price":456.25,"market_rates":[{"supplier":"expedia","rate":456.245880748}]},{"id":"VhoE","searchRank":0.94,"price_type":"multi","max_cash_payment":165.98,"coverted_max_cash_payment":233.35,"points":5825,"bonuses":0,"lowest_price":165.98,"price":233.35,"converted_price":233.35,"lowest_converted_price":233.35,"market_rates":[{"supplier":"expedia","rate":203.182098748}]},{"id":"S57Q","searchRank":2,"price_type":"multi","max_cash_payment":247.62,"coverted_max_cash_payment":348.13,"points":8700,"bonuses":0,"lowest_price":247.62,"price":348.13,"converted_price":348.13,"lowest_converted_price":348.13,"market_rates":[]},{"id":"wcfx","searchRank":0.94,"price_type":"multi","max_cash_payment":590.17,"coverted_max_cash_payment":829.73,"points":20725,"bonuses":0,"lowest_price":590.17,"price":829.73,"converted_price":829.73,"lowest_converted_price":829.73,"market_rates":[{"supplier":"expedia","rate":723.5937073319999}]},{"id":"cETW","searchRank":2,"price_type":"multi","max_cash_payment":126.05,"coverted_max_cash_payment":177.21,"points":4425,"bonuses":0,"lowest_price":126.05,"price":177.21,"converted_price":177.21,"lowest_converted_price":177.21,"market_rates":[]}]
    const test_hoteldetails = TestingHotelDetails;
    const data = await HotelPerPage(test_hotelList,test_hoteldetails);
    expect(data.length).toEqual(test_hotelList.length);
})