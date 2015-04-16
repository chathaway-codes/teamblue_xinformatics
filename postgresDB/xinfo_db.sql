--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: coursereqs; Type: TABLE; Schema: public; Owner: mcguik2; Tablespace: 
--

CREATE TABLE coursereqs (
    coursename character varying(255),
    req1 character varying(255),
    req2 character varying(255),
    req3 character varying(255)
);


ALTER TABLE public.coursereqs OWNER TO mcguik2;

--
-- Name: courses; Type: TABLE; Schema: public; Owner: mcguik2; Tablespace: 
--

CREATE TABLE courses (
    crnsec character varying(255),
    crn integer,
    courseid character varying(255),
    course_title character varying(255),
    class_type character varying(255),
    credit_hours integer,
    days character varying(255),
    start_time character varying(255),
    end_time character varying(255),
    ampm character varying(255),
    instructor character varying(255),
    building character varying(255),
    classroom character varying(255),
    max_enrollment integer,
    enrolled integer,
    seats_remaining integer,
    textbook_url character varying(1023)
);


ALTER TABLE public.courses OWNER TO mcguik2;

--
-- Data for Name: coursereqs; Type: TABLE DATA; Schema: public; Owner: mcguik2
--

COPY coursereqs (coursename, req1, req2, req3) FROM stdin;
CSCI-1100 Computer Science I	none	none	none
MATH-1010 Calculus I	none	none	none
PHYS-1100 Physics I	none	none	none
CSCI-1200 Data Structures	CSCI-1100	none	none
MATH-1020 Calculus II	MATH-1010	none	none
BIOL-1010 Introduction to Biology	none	none	none
BIOL-1015 Introduction to Biology Lab	none	none	none
CSCI-2200 Foundations of Computer Science	MATH-1010	CSCI-1100	none
CSCI-2500 Computer Organization	CSCI-1200	none	none
CSCI-2300 Introduction to Algorithms	CSCI-1200	MATH-1010	CSCI-2200
CSCI-2300 Introduction to Algorithms	CSCI-1200	MATH-1010	MATH-2800
CSCI-2600 Principles of Software	CSCI-1200	none	none
CSCI-4430 Programming Languages	CSCI-2300	none	none
CSCI-4210 Operating Systems	CSCI-2300	CSCI-2500	none
CSCI-4440 Software Design and Documentation	CSCI-2300	none	none
\.


--
-- Data for Name: courses; Type: TABLE DATA; Schema: public; Owner: mcguik2
--

COPY courses (crnsec, crn, courseid, course_title, class_type, credit_hours, days, start_time, end_time, ampm, instructor, building, classroom, max_enrollment, enrolled, seats_remaining, textbook_url) FROM stdin;
65648 CSCI-1010-01	65648	CSCI-1010	INTRO TO COMPUTER PROGRAMMING	LEC	4	M R	8:00	9:50	AM	Kuchera	LALLY	102	50	30	20	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=1010&section-1=01
66435 CSCI-1010-02	66435	CSCI-1010	INTRO TO COMPUTER PROGRAMMING	LEC	4	M R	6:00	7:50	PM	Schoch	LALLY	102	50	35	15	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=1010&section-1=02
65049 CSCI-1100-01	65049	CSCI-1100	COMPUTER SCIENCE I	LEC	4	M R	2:00	3:20	PM	Adali	DARRIN	308	35	30	5	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=1100&section-1=01
65050 CSCI-1100-02	65050	CSCI-1100	COMPUTER SCIENCE I	LEC	4	M R	2:00	3:20	PM	Adali	DARRIN	308	45	32	13	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=1100&section-1=02
65051 CSCI-1100-03	65051	CSCI-1100	COMPUTER SCIENCE I	LEC	4	M R	2:00	3:20	PM	Adali	DARRIN	308	45	44	1	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=1100&section-1=03
65052 CSCI-1100-04	65052	CSCI-1100	COMPUTER SCIENCE I	LEC	4	M R	2:00	3:20	PM	Adali	DARRIN	308	40	32	8	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=1100&section-1=04
65053 CSCI-1100-05	65053	CSCI-1100	COMPUTER SCIENCE I	LEC	4	M R	2:00	3:20	PM	Adali	DARRIN	308	40	37	3	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=1100&section-1=05
66573 CSCI-1100-06	66573	CSCI-1100	COMPUTER SCIENCE I	LEC	4	M R	2:00	3:20	PM	Adali	DARRIN	308	30	28	2	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=1100&section-1=06
65470 CSCI-1100-07	65470	CSCI-1100	COMPUTER SCIENCE I	LEC	4	M R	2:00	3:20	PM	Adali	DARRIN	308	30	25	5	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=1100&section-1=07
65471 CSCI-1100-08	65471	CSCI-1100	COMPUTER SCIENCE I	LEC	4	M R	2:00	3:20	PM	Adali	DARRIN	308	30	30	0	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=1100&section-1=08
66238 CSCI-1100-09	66238	CSCI-1100	COMPUTER SCIENCE I	LEC	4	M R	2:00	3:20	PM	Adali	DARRIN	308	30	27	3	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=1100&section-1=09
66581 CSCI-1100-10	66581	CSCI-1100	COMPUTER SCIENCE I	LEC	4	M R	2:00	3:20	PM	Adali	DARRIN	308	40	22	18	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=1100&section-1=10
66808 CSCI-1100-11	66808	CSCI-1100	COMPUTER SCIENCE I	LEC	4	M R	2:00	3:20	PM	Adali	DARRIN	308	40	35	5	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=1100&section-1=11
67351 CSCI-1100-12	67351	CSCI-1100	COMPUTER SCIENCE I	LEC	4	M R	2:00	3:20	PM	Adali	DARRIN	308	32	17	15	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=1100&section-1=12
67819 CSCI-1100-13	67819	CSCI-1100	COMPUTER SCIENCE I	LEC	4	M R	2:00	3:20	PM	Adali	DARRIN	308	45	29	16	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=1100&section-1=13
67820 CSCI-1100-14	67820	CSCI-1100	COMPUTER SCIENCE I	LEC	4	M R	2:00	3:20	PM	Adali	DARRIN	308	30	25	5	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=1100&section-1=14
68256 CSCI-1100-15	68256	CSCI-1100	COMPUTER SCIENCE I	LEC	4	M R	2:00	3:20	PM	Adali	DARRIN	308	30	22	8	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=1100&section-1=15
67217 CSCI-1190-01	67217	CSCI-1190	BEGINNING PROG FOR ENG	LEC	1	T	6:00	7:50	PM	Todd	SAGE	5101	58	50	8	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=1190&section-1=01
67218 CSCI-1190-02	67218	CSCI-1190	BEGINNING PROG FOR ENG	LEC	1	W	6:00	7:50	PM	Todd	SAGE	5101	58	53	5	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=1190&section-1=02
67220 CSCI-1190-03	67220	CSCI-1190	BEGINNING PROG FOR ENG	LEC	1	R	6:00	7:50	PM	Todd	SAGE	5101	58	54	4	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=1190&section-1=03
67219 CSCI-1190-04	67219	CSCI-1190	BEGINNING PROG FOR ENG	LEC	1	M	6:00	7:50	PM	Staff	SAGE	5101	58	59	-1	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=1190&section-1=04
67880 CSCI-1190-05	67880	CSCI-1190	BEGINNING PROG FOR ENG	LEC	1	T	6:00	7:50	PM	Staff	SAGE	5101	58	58	0	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=1190&section-1=05
67581 CSCI-1190-06	67581	CSCI-1190	BEGINNING PROG FOR ENG	LEC	1	R	6:00	7:50	PM	Staff	SAGE	5101	58	58	0	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=1190&section-1=06
66574 CSCI-1200-01	66574	CSCI-1200	DATA STRUCTURES	LEC	4	T F	2:00	3:50	PM	Cutler	SAGE	3303	35	34	1	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=1200&section-1=01
65054 CSCI-1200-02	65054	CSCI-1200	DATA STRUCTURES	LAB	4	W	10:00	11:5	0A	Staff	LALLY	104	35	31	4	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=1200&section-1=02
65055 CSCI-1200-03	65055	CSCI-1200	DATA STRUCTURES	LAB	4	W	12:00	1:50	PM	Staff	LALLY	104	35	30	5	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=1200&section-1=03
65056 CSCI-1200-04	65056	CSCI-1200	DATA STRUCTURES	LEC	4	T F	2:00	3:50	PM	Cutler	SAGE	3303	35	36	-1	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=1200&section-1=04
65436 CSCI-1200-05	65436	CSCI-1200	DATA STRUCTURES	LEC	4	T F	2:00	3:50	PM	Cutler	SAGE	3303	35	33	2	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=1200&section-1=05
68069 CSCI-1200-06	68069	CSCI-1200	DATA STRUCTURES	LEC	4	T F	2:00	3:50	PM	Cutler	SAGE	3303	35	32	3	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=1200&section-1=06
68750 CSCI-1200-07	68750	CSCI-1200	DATA STRUCTURES	LEC	4	T F	2:00	3:50	PM	Cutler	SAGE	3303	35	34	1	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=1200&section-1=07
68077 CSCI-2200-01	68077	CSCI-2200	FOUNDATIONS OF COMPUTER SCI	LEC	4	M R	10:00	11:5	0A	Magdon-Ism	SAGE	3303	80	76	4	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=2200&section-1=01
68591 CSCI-2200-02	68591	CSCI-2200	FOUNDATIONS OF COMPUTER SCI	LEC	4	M R	10:00	11:5	0A	Magdon-Ism	SAGE	3303	80	70	10	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=2200&section-1=02
68592 CSCI-2200-03	68592	CSCI-2200	FOUNDATIONS OF COMPUTER SCI	LEC	4	M R	10:00	11:5	0A	Magdon-Ism	SAGE	3303	70	75	-5	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=2200&section-1=03
65057 CSCI-2300-01	65057	CSCI-2300	INTRODUCTION TO ALGORITHMS	LEC	4	M R	12:00	1:20	PM	Krishnamoo	DARRIN	318	33	20	13	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=2300&section-1=01
65058 CSCI-2300-02	65058	CSCI-2300	INTRODUCTION TO ALGORITHMS	LEC	4	M R	12:00	1:20	PM	Krishnamoo	DARRIN	318	33	21	12	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=2300&section-1=02
65437 CSCI-2300-03	65437	CSCI-2300	INTRODUCTION TO ALGORITHMS	LEC	4	M R	12:00	1:20	PM	Krishnamoo	DARRIN	318	33	15	18	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=2300&section-1=03
65420 CSCI-2300-04	65420	CSCI-2300	INTRODUCTION TO ALGORITHMS	LEC	4	M R	12:00	1:20	PM	Krishnamoo	DARRIN	318	33	29	4	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=2300&section-1=04
66544 CSCI-2300-05	66544	CSCI-2300	INTRODUCTION TO ALGORITHMS	LEC	4	M R	12:00	1:20	PM	Krishnamoo	DARRIN	318	33	17	16	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=2300&section-1=05
65368 CSCI-2300-06	65368	CSCI-2300	INTRODUCTION TO ALGORITHMS	LEC	4	M R	12:00	1:20	PM	Krishnamoo	DARRIN	318	33	17	16	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=2300&section-1=06
65059 CSCI-2500-01	65059	CSCI-2500	COMPUTER ORGANIZATION	LEC	4	T F	12:00	1:50	PM	Liu	DARRIN	318	140	139	1	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=2500&section-1=01
68572 CSCI-2600-01	68572	CSCI-2600	PRINCIPLES OF SOFTWARE	LEC	4	T F	2:00	3:50	PM	Milanova	LOW	3112	25	27	-2	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=2600&section-1=01
68632 CSCI-2960-01	68632	CSCI-2960	WEB SYSTEMS DEVELOPMENT	LEC	4	M R	4:00	5:50	PM	Plotka	LALLY	104	5	6	-1	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=2960&section-1=01
67525 CSCI-2961-01	67525	CSCI-2961	PROGRAMMING IN PYTHON	LEC	2	T	6:00	7:50	PM	Thompson	WALKER	5113	50	51	-1	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=2961&section-1=01
65472 CSCI-4050-01	65472	CSCI-4050	COMPUT. & COMPLEXITY	LEC	4	M R	2:00	3:50	PM	Goldberg	TROY	2018	60	8	52	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4050&section-1=01
66577 CSCI-4100-01	66577	CSCI-4100	MACHINE LEARNING	LEC	4	T F	12:00	1:50	PM	Magdon-Ism	SAGE	5101	50	42	8	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4100&section-1=01
66982 CSCI-4150-01	66982	CSCI-4150	INTRO TO ARTIFICIAL INTELLIG	LEC	4	T F	10:00	11:5	0A	Macdonald	LOW	3051	70	67	3	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4150&section-1=01
65060 CSCI-4210-01	65060	CSCI-4210	OPERATING SYSTEMS	LEC	4	M R	2:00	3:50	PM	Goldschmid	RCKTTS	203	118	108	10	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4210&section-1=01
68552 CSCI-4230-01	68552	CSCI-4230	CRYPT & NETWORK SECURITY I	LEC	3	W	10:00	12:5	0P	Yener	TROY	2018	50	29	21	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4230&section-1=01
68540 CSCI-4350-01	68540	CSCI-4350	DATA SCIENCE	LEC	3	T	9:00	11:5	0A	Fox	LALLY	102	0	5	-5	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4350&section-1=01
65477 CSCI-4380-01	65477	CSCI-4380	DATABASE SYSTEMS	LEC	4	M R	12:00	1:50	PM	Hardwick	SAGE	5101	70	70	0	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4380&section-1=01
68574 CSCI-4390-01	68574	CSCI-4390	DATABASE MINING	LEC	4	T F	10:00	11:5	0A	Liu	SAGE	5510	65	16	49	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4390&section-1=01
65702 CSCI-4430-01	65702	CSCI-4430	PROGRAMMING LANGUAGES	LEC	4	T F	2:00	3:50	PM	Varela	DARRIN	318	105	100	5	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4430&section-1=01
65107 CSCI-4440-01	65107	CSCI-4440	SOFTWARE DESIGN & DOC.	LEC	4	M R	4:00	5:50	PM	Sturman	WALKER	6113	50	47	3	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4440&section-1=01
65224 CSCI-4440-02	65224	CSCI-4440	SOFTWARE DESIGN & DOC.	LEC	4	M R	6:00	7:50	PM	Sturman	WALKER	6113	25	24	1	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4440&section-1=02
65468 CSCI-4440-03	65468	CSCI-4440	SOFTWARE DESIGN & DOC.	LEC	4	M R	6:00	7:50	PM	Sturman	WALKER	6113	25	26	-1	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4440&section-1=03
66809 CSCI-4480-01	66809	CSCI-4480	ROBOTICS I	LEC	3	M R	12:30	1:50	PM	Wu	LALLY	104	40	8	32	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4480&section-1=01
66978 CSCI-4520-01	66978	CSCI-4520	GAME DEVELOPMENT I	LEC	4	W	2:00	5:50	PM	Destefano	TROY	2012	19	20	-1	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4520&section-1=01
66180 CSCI-4650-01	66180	CSCI-4650	NETWORKING LABORATORY I	LEC	4	T R	6:00	7:50	PM	Kotfila/Price	EATON	215	100	31	69	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4650&section-1=01
66181 CSCI-4660-01	66181	CSCI-4660	NETWORKING LABORATORY II	LEC	4	T	6:00	8:50	PM	Kotfila	EATON	216	25	10	15	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4660&section-1=01
65231 CSCI-4800-01	65231	CSCI-4800	NUMERICAL COMPUTING	LEC	4	M R	10:00	11:5	0A	Lai	CARNEG	201	40	6	34	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4800&section-1=01
67479 CSCI-4800-02	67479	CSCI-4800	NUMERICAL COMPUTING	LEC	4	T F	10:00	11:5	0A	Foster	SAGE	5101	50	12	38	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4800&section-1=02
67786 CSCI-4960-01	67786	CSCI-4960	INTERACTIVE VISUALIZATION	LEC	4	T F	12:00	1:50	PM	Cutler	LALLY	2	15	16	-1	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4960&section-1=01
66942 CSCI-4961-01	66942	CSCI-4961	DISTR COMPUTING ON INTERNET	LEC	4	M R	10:00	11:5	0A	Varela	CARNEG	210	20	1	19	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4961&section-1=01
68078 CSCI-4962-01	68078	CSCI-4962	NATURAL LANGUAGE PROCESSING	LEC	4	W	1:00	3:50	PM	Ji	CARNEG	112	20	16	4	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4962&section-1=01
67469 CSCI-4963-01	67469	CSCI-4963	THEORY OF NETWORKED SYSTEMS	LEC	4	M R	12:00	1:50	PM	Patterson	SAGE	5510	20	9	11	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4963&section-1=01
66192 CSCI-4964-01	66192	CSCI-4964	ADV NETWORK PRACTICUM	LEC	4	T	6:00	8:50	PM	Kotfila	LALLY	104	10	0	10	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4964&section-1=01
68567 CSCI-4965-01	68567	CSCI-4965	RCOS	LEC	0	T F	4:00	5:50	PM	Goldschmid	EATON	214	100	96	4	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4965&section-1=01
66437 CSCI-4966-01	66437	CSCI-4966	PROGRAMMING FOR COG SCI & AI	LEC	4	T F	2:00	3:50	PM	Schoelles	SAGE	2112	6	8	-2	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4966&section-1=01
65577 CSCI-4970-01	65577	CSCI-4970	COMPUTER NETWORK LAB	LAB	0	M	4:00	5:50	PM	Kotfila	EATON	215	16	11	5	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4970&section-1=01
65578 CSCI-4970-02	65578	CSCI-4970	COMPUTER NETWORK LAB	LAB	0	M	8:00	9:50	PM	Kotfila	EATON	215	16	3	13	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4970&section-1=02
65579 CSCI-4970-03	65579	CSCI-4970	COMPUTER NETWORK LAB	LAB	0	T	4:00	5:50	PM	Kotfila	EATON	215	16	13	3	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4970&section-1=03
65580 CSCI-4970-04	65580	CSCI-4970	COMPUTER NETWORK LAB	LAB	0	T	8:00	9:50	PM	Kotfila	EATON	215	16	7	9	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4970&section-1=04
65581 CSCI-4970-05	65581	CSCI-4970	COMPUTER NETWORK LAB	LAB	0	W	2:00	3:50	PM	Kotfila	SAGE	2707	16	9	7	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4970&section-1=05
65582 CSCI-4970-06	65582	CSCI-4970	COMPUTER NETWORK LAB	LAB	0	W	4:00	5:50	PM	Kotfila	LOW	4040	16	14	2	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4970&section-1=06
65583 CSCI-4970-07	65583	CSCI-4970	COMPUTER NETWORK LAB	LAB	0	W	8:00	9:50	PM	Kotfila	EATON	215	16	5	11	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4970&section-1=07
65584 CSCI-4970-08	65584	CSCI-4970	COMPUTER NETWORK LAB	LAB	0	R	4:00	5:50	PM	Kotfila	EATON	215	16	2	14	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4970&section-1=08
65585 CSCI-4970-09	65585	CSCI-4970	COMPUTER NETWORK LAB	LAB	0	R	8:00	9:50	PM	Kotfila	EATON	215	16	11	5	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4970&section-1=09
67787 CSCI-4972-01	67787	CSCI-4972	AFFECTIVE COMPUTING	LEC	4	M R	4:00	5:50	PM	Si	CARNEG	113	15	10	5	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4972&section-1=01
68247 CSCI-4979-01	68247	CSCI-4979	COMPUTATIONAL SOCIAL CHOICE	LEC	4	M R	12:00	1:50	PM	Xia	CARNEG	206	8	2	6	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=4979&section-1=01
65423 CSCI-6050-01	65423	CSCI-6050	COMPUTABILITY & COMPLEXITY	LEC	3	M R	2:00	3:50	PM	Goldberg	TROY	2018	60	18	42	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=6050&section-1=01
66578 CSCI-6100-01	66578	CSCI-6100	MACHINE LEARNING	LEC	3	T F	12:00	1:50	PM	Magdon-Ism	SAGE	5101	30	43	-13	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=6100&section-1=01
65061 CSCI-6140-01	65061	CSCI-6140	COMPUTER OPERATING SYSTEMS	LEC	3	M R	2:00	3:50	PM	Goldschmid	RCKTTS	203	30	26	4	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=6140&section-1=01
68566 CSCI-6230-01	68566	CSCI-6230	CRYPT AND NETWORK SECURITY I	LEC	3	W	10:00	12:5	0P	Yener	TROY	2018	50	10	40	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=6230&section-1=01
68541 CSCI-6350-01	68541	CSCI-6350	DATA SCIENCE	LEC	3	T	9:00	11:5	0A	Fox	LALLY	102	30	11	19	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=6350&section-1=01
68575 CSCI-6390-01	68575	CSCI-6390	DATABASE MINING	LEC	3	T F	10:00	11:5	0A	Liu	SAGE	5510	30	25	5	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=6390&section-1=01
68551 CSCI-6430-01	68551	CSCI-6430	PROGRAMMING LANGUAGES	LEC	3	T F	2:00	3:50	PM	Varela	DARRIN	318	20	6	14	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=6430&section-1=01
68558 CSCI-6500-01	68558	CSCI-6500	DISTR COMPUTING ON INTERNET	LEC	3	M R	10:00	11:5	0A	Varela	CARNEG	210	20	4	16	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=6500&section-1=01
65654 CSCI-6800-01	65654	CSCI-6800	COMPUTATIONAL LINEAR ALGEBRA	LEC	4	M R	10:00	11:5	0A	Henshaw	CARNEG	113	25	7	18	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=6800&section-1=01
65478 CSCI-6900-01	65478	CSCI-6900	COMPUTER SCIENCE SEMINAR	LEC	0	T	3:30	4:50	PM	Goldschmid	LOW	3051	50	0	50	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=6900&section-1=01
66961 CSCI-6961-01	66961	CSCI-6961	AFFECTIVE COMPUTING	LEC	3	M R	4:00	5:50	PM	Si	CARNEG	113	10	1	9	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=6961&section-1=01
66748 CSCI-6962-01	66748	CSCI-6962	NATURAL LANGUAGE PROCESSING	LEC	3	W	1:00	3:50	PM	Ji	CARNEG	112	10	11	-1	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=6962&section-1=01
66962 CSCI-6963-01	66962	CSCI-6963	THEORY OF NETWORKED SYSTEMS	LEC	3	M R	12:00	1:50	PM	Patterson	SAGE	5510	20	11	9	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=6963&section-1=01
68658 CSCI-6964-01	68658	CSCI-6964	FRONTIERS OF NETWORK SCIENCE	LEC	3	W	1:00	3:50	PM	Szymanski	DARRIN	236	16	16	0	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=6964&section-1=01
65623 CSCI-6968-01	65623	CSCI-6968	NETWORKING LABORATORY I	LEC	3	T R	6:00	7:50	PM	Kotfila/Price	EATON	215	10	0	10	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=6968&section-1=01
65540 CSCI-6969-01	65540	CSCI-6969	NETWORKING LABORATORY II		3	T	6:00	8:50	PM	Staff	EATON	215	10	0	10	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=6969&section-1=01
68248 CSCI-6976-01	68248	CSCI-6976	COMPUTATIONAL SOCIAL CHOICE	LEC	3	M R	12:00	1:50	PM	Xia	CARNEG	206	12	9	3	http://www.bkstr.com/webapp/wcs/stores/servlet/booklookServlet?bookstore_id-1=70063&term_id-1=Fall-14-Troy&div-1=&dept-1=CSCI&course-1=6976&section-1=01
\.


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

