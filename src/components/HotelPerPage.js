const sleep = require('util').promisify(setTimeout)

export async function HotelPerPage(props, HotelDetails){
    var hotelListSlice = [];
    var seen = {};
    const HotelPriceList = props.filter(function(item) {
        return seen.hasOwnProperty(item.id) ? false : (seen[item.id] = true);
    });
    
    if (HotelPriceList.length === 0){
            return hotelListSlice;};
    for (let i=0;i<HotelPriceList.length;i++){
        let hotel = HotelPriceList[i];
        let data = HotelDetails.find(item => item.id === hotel.id);
        if (data == null) {
            let payload = {}
            payload.url = `https://hotelapi.loyalty.dev/api/hotels/${hotel.id}`        
            let res = await fetch("http://localhost:5000/apis/hotelDetail", {
                method: 'POST',
                headers: {'Content-Type':'application/json'}, // this line is important, if this content-type is not set it wont work
                body: JSON.stringify(payload)
            });
            data = await res.json();
            (async () => {
                await sleep(400)
            })()
        }
        data["price"]=hotel.lowest_price ;
        data["searchRank"]=hotel.searchRank;
        data["rooms"]=hotel.rooms
        hotelListSlice.push(data);
    }
    return hotelListSlice;
}