-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT * FROM crime_scene_reports WHERE street = 'Humphrey Street';

SELECT * FROM interviews WHERE transcript LIKE '%bakery%';

SELECT * FROM bakery_security_logs WHERE (year = 2021) AND (month = 7) AND (day = 28) AND (hour = 10) AND (minute >= 15 AND minute <= 25);

SELECT p.name, bsl.activity, bsl.license_plate, bsl.year, bsl.month, bsl.day, bsl.hour, bsl.minute
JOIN people p ON p.license_plate = bsl.license_plate
WHERE bsl.year = 2021 AND bsl.month = 7 AND bsl.day = 28 AND bsl.hour = 10 AND bsl.minute BETWEEN 15 AND 25;

SELECT * FROM atm_transactions WHERE atm_location = 'Leggett Street'
AND year = 2021 AND month = 7 AND day = 28;

SELECT atm.*, p.name
FROM atm_transactions atm
JOIN bank_accounts bank ON atm.account_member = bank.account_number
JOIN people peop ON bank.person_id = peop.id
WHERE atm.atm_location = 'Leggett Street' AND atm.year = 2021 AND atm.month = 7 AND atm.day = 28 AND atm.transcation_type = 'withdraw';

SELECT *
FROM phone_calls
WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;

SELECT p.name, pc.caller, pc.receiver, pc.year, pc.month, pc.dat, pc.duration
FROM phone_calls pc
JOIN people p ON pc.caller = p.phone_number
WHERE pc.year = 2021 AND pc.month = 7 AND pc.day = 28 AND pc.duration < 60;

SELECT * FROM airports;

SELECT f.*, origin.full_name AS origin_airport, destination.full_name AS destination_airport
FROM flights f
JOIN airports origin ON f.origin_airport_id = origin.id
JOIN airports destination ON f.destination_airport_id = destination.id
WHERE origin.id = 8 AND f.year = 2021 AND f.month = 7 AND f.day = 29
ORDER BY f.hour, f.minute;

SELECT p.name
FROM people.p
JOIN passengers ps ON p.passport_number = ps.passport_number
WHERE ps.flight_id = 36
AND p.name IN ('Bruce', 'Diana');
