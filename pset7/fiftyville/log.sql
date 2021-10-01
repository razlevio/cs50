-- log of any SQL queries I executed as I solve the mystery:
------------------------------------------------------------

-- Checking the crime scene report from the day of the CS50 duck theft
--SELECT description FROM crime_scene_reports
--  WHERE year = 2020 AND month = 07 AND day = 28 AND street LIKE 'Chamberlin%'
-- The theft hapened in Chamberlin Street Courthouse at 10:15AM, there was three witnesses that were interviewd


-- Checcking the transcripts of the interviews to see clues
-- SELECT name, transcript FROM interviews
--  WHERE year = 2020 AND month = 07 AND day = 28;

/*
   Clue 1: Theif get into a car in courthouse parking lot in somewhere withing 10 minutes from the theft
           CHECK FOR CARS FROM FOOTAGE THAT left the parking lot between 10:15AM to 10:25AM

   Clue 2: Between 10:15AM to 10:25AM the theif CALLED the accomplice and they talked over the phone they talked for less than minute
           On the phone call the theif plans to take the EARLIEST flight on the following day July 29 2020
           The theif accomplice bought the tickets for the Theif

   Clue 3: Before 10:15AM the theif withdraw money from Fifer Street ATM
*/

---------------------------------------------------------------------------------------------------------------------------------------------
--                                                          CLUES INVASTIGATING:                                                           --
---------------------------------------------------------------------------------------------------------------------------------------------


-- Clue 1 Checking, investigating the courthouse security logs checking the license plates of vehciles that exit the parking lot
SELECT license_plate FROM courthouse_security_logs
WHERE activity = 'exit' AND year = 2020 AND month = 07 AND day = 28 AND hour = 10 AND minute BETWEEN 15 AND 25;

-- Possible licences plates = 5P2BI95 94KL13X 6P58WS2 4328GD8 G412CB7 L93JTIZ 322W7JE 0NTHK55
-- Checking id, name, phone num, passport number and license plate of people with licneses plates thast exit the parking lot within the time frame
 SELECT id, name, phone_number, passport_number, license_plate FROM people
  WHERE license_plate IN ('5P2BI95', '94KL13X', '6P58WS2', '4328GD8', 'G412CB7', 'L93JTIZ', '322W7JE', '0NTHK55');
/*
        id | name      | phone_number   | passport_number | license_plate
    221103 | Patrick   | (725) 555-4692 | 2963008352      | 5P2BI95
    243696 | Amber     | (301) 555-4174 | 7526138472      | 6P58WS2
    396669 | Elizabeth | (829) 555-5269 | 7049073643      | L93JTIZ
    398010 | Roger     | (130) 555-0289 | 1695452385      | G412CB7    **
    467400 | Danielle  | (389) 555-5198 | 8496433585      | 4328GD8
    514354 | Russell   | (770) 555-1861 | 3592750733      | 322W7JE    **
    560886 | Evelyn    | (499) 555-9472 | 8294398571      | 0NTHK55    **
    686048 | Ernest    | (367) 555-5533 | 5773159633      | 94KL13X    **
*/

-- Comparing the phone numbers to the ones I found below in Clue 2 checking to find out the owners of vehicles that talked on the phone
-- When the theif leave the parking lot and the license plate one of the cars that exit the parkinglot,
-- that is means that the theif is one of those, the theif own the vehcile and was the phone caller

SELECT DISTINCT p.id, p.name, p.phone_number, p.passport_number, p.license_plate FROM people AS p
        INNER JOIN phone_calls AS pc
        ON pc.caller = p.phone_number
    WHERE p.license_plate IN ('5P2BI95', '94KL13X', '6P58WS2', '4328GD8', 'G412CB7', 'L93JTIZ', '322W7JE', '0NTHK55')
    AND pc.year = 2020 AND pc.month = 07 AND pc.day = 28 AND pc.duration < 60;

/*
    id | name    | phone_number   | passport_number | license_plate
398010 | Roger   | (130) 555-0289 | 1695452385      | G412CB7
514354 | Russell | (770) 555-1861 | 3592750733      | 322W7JE
560886 | Evelyn  | (499) 555-9472 | 8294398571      | 0NTHK55
686048 | Ernest  | (367) 555-5533 | 5773159633      | 94KL13X
*/

-- Clue 2 Checking, Investigating phone calls between 10:15AM and 10:25AM DURATION less than 1 min
SELECT caller, receiver FROM phone_calls
WHERE year = 2020 AND month = 07 AND day = 28 AND duration < 60;
/* Possible phone numbers               caller | receiver
                                (130) 555-0289 | (996) 555-8899
                                (499) 555-9472 | (892) 555-8872
                                (367) 555-5533 | (375) 555-8161
                                (499) 555-9472 | (717) 555-1342
                                (286) 555-6063 | (676) 555-6554
                                (770) 555-1861 | (725) 555-3243
                                (031) 555-6622 | (910) 555-3251
                                (826) 555-1652 | (066) 555-9701
                                (338) 555-6650 | (704) 555-2131  */

-- Clue 3 Checking, looking for account nums withdrawls before 10:15AM from Fifer Street
SELECT account_number FROM atm_transactions
WHERE transaction_type LIKE '_ithdraw%' AND year = 2020 AND month = 07 AND day = 28 AND atm_location LIKE 'Fifer%'
-- Possible Account Numbers: 28500762 28296815 76054385 49610011 16153065 25506511 81061156 26013199

-- Checking information of people with the bank accounts I found above
SELECT p.id, p.name, p.phone_number, p.passport_number, p.license_plate
    FROM people AS p
    INNER JOIN bank_accounts AS b
    ON p.id = b.person_id
    WHERE account_number IN (28500762,28296815,76054385,49610011,16153065,25506511,81061156,26013199);

/* Possible Theif or Accomplice: THE RECORDS WITH * matched with caller phone numbers from Clue 2. MUST BE THEIF
    name      | phone_number   | passport_number | license_plate
  * Ernest    | (367) 555-5533 | 5773159633      | 94KL13X
  * Russell   | (770) 555-1861 | 3592750733      | 322W7JE
    Roy       | (122) 555-4581 | 4408372428      | QX4YZN3
  * Bobby     | (826) 555-1652 | 9878712108      | 30G67EN
    Elizabeth | (829) 555-5269 | 7049073643      | L93JTIZ
    Danielle  | (389) 555-5198 | 8496433585      | 4328GD8
  * Madison   | (286) 555-6063 | 1988161715      | 1106N58
  * Victoria  | (338) 555-6650 | 9586786673      | 8X428L0 
  
  Since Ernest and Russell was one of the car owners and one of the phone callers they become theif most suspects
  */


-- Clue 3 Checking, Look up what is the EARLIEST flight on the July 29 2020 recall the theif accomplice bought the tickets for the Theif
-- Checking the first flight hour which is : 08:20 AM and this flight id: 36, destination air port id: 4
SELECT f.hour, f.minute, a.city, a.full_name, f.id AS flight_ID, f.destination_airport_id FROM flights AS f
        INNER JOIN airports AS a ON f.origin_airport_id = a.id
    WHERE a.city LIKE 'Fifty%' AND f.year = 2020 AND f.month = 07 AND f.day = 29
    ORDER BY f.hour LIMIT 1;
-- Checking the desnenation city based on the flight
SELECT full_name, city FROM airports
WHERE id = 4;
-- The first flight ID 36 from Fiftyville to London, Heatthrow Airport


-- Checking the passport numbers of the people that were on the flight to london flight 36
SELECT p1.passport_number, p2.name
    FROM passengers AS p1
    INNER JOIN people AS p2
    ON p1.passport_number = p2.passport_number
WHERE p1.flight_id = 36 AND p1.passport_number IN (1695452385, 3592750733, 8294398571, 5773159633);

/*
    One of them is the theif
    1695452385 | Roger
    5773159633 | Ernest
    8294398571 | Evelyn
    
    Since I found out that the theif most be Russel or Ernest now I know that the Theif is Ernest.
*/

-- Checking who is the person that talk with Ernest in the phone call, since I know that Ernest is the caller
-- And the reciever is the accomplice I will check who is the person that talk with ernest using the phone nuber from the phone calls
SELECT pc.id, pc.caller, pc.receiver, p.name, p.phone_number FROM phone_calls AS pc
    INNER JOIN people AS p
    ON pc.receiver = p.phone_number AND pc.caller = '(367) 555-5533'
WHERE year = 2020 AND month = 07 AND day = 28 AND duration < 60;

-- The THIEF is: Ernest
-- The thief ESCAPED TO: London
-- The ACCOMPLICE is: Berthold