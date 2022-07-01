import {Card, Col, Row} from 'antd';

// import { useSelector, useDispatch } from 'react-redux';
const fakeData = {
    hotelstar: 4,
    hotelgrade: "Good",
    hotelName: "Fullerton Hotel Singapore",
    roomType: "Deluxe Plus",
    numberOfRoom: 2,
    numberOfAdult: 2,
    numberOfChildren: 2,
    checkinDate: "10/12/2022",
    checkoutDate: "11/12/2022",
    totalCost: 12.40
}



const BookingSummary = () => {

    return (
        <Row>
            <Col span={10} offset={7} style={{marginTop: 16, marginBottom: 16}}>
                <Card title= {<h3> <b> Hotel Ratings</b></h3>} >
                    <div style={{textAlign: "left"}}>
                        <Row>
                            <Col span ={7} offset= {5}>
                                <p> <b>Number of stars:</b> {fakeData.hotelstar}</p> 
                            </Col>
                            <Col span ={7} offset= {2}>
                                <p> <b>Hotel Grade :</b> {fakeData.hotelgrade}</p>
                            </Col>
                        </Row>
                        
                        
                    </div>
                </Card>
            </Col>
        </Row>
    )
}

export default BookingSummary;