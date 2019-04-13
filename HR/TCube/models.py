# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Academic(models.Model):
    instituteid = models.IntegerField()
    streamid = models.IntegerField(blank=True, null=True)
    head_title = models.IntegerField(blank=True, null=True)
    headname = models.CharField(max_length=150, blank=True, null=True)
    heademail = models.CharField(max_length=100, blank=True, null=True)
    head_designation = models.IntegerField(blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    headaddress = models.TextField(blank=True, null=True)
    isactive = models.IntegerField(db_column='isActive', blank=True, null=True)  # Field name made lowercase.
    last_update = models.DateTimeField()
    head_contact = models.CharField(max_length=20, blank=True, null=True)
    last_updatedby = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'academic'


class Accomodation(models.Model):
    participantid = models.ForeignKey('Participant', db_column='participantid', primary_key=True)
    workshopid = models.IntegerField(blank=True, null=True)
    instituteid = models.IntegerField(blank=True, null=True)
    accomodation = models.CharField(max_length=20, blank=True, null=True)
    acc_old = models.CharField(max_length=20, blank=True, null=True)
    ins_same_as_rc = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accomodation'


class AfApplicants(models.Model):
    personid = models.ForeignKey('Person', db_column='personid')
    workshopid = models.ForeignKey('Workshops', db_column='workshopid')
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'af_applicants'
        unique_together = (('personid', 'workshopid'),)


class AfSelected(models.Model):
    personid = models.ForeignKey('Person', db_column='personid')
    workshopid = models.ForeignKey('Workshops', db_column='workshopid')
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'af_selected'
        unique_together = (('personid', 'workshopid'),)


class Announcement(models.Model):
    announcementid = models.IntegerField(primary_key=True)
    type = models.IntegerField(blank=True, null=True)
    announcement = models.CharField(max_length=450, blank=True, null=True)
    link = models.CharField(max_length=250, blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=40)
    location = models.CharField(max_length=100)
    visible = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'announcement'


class Attendance(models.Model):
    workshopid = models.IntegerField()
    participantid = models.ForeignKey('Participant', db_column='participantid')
    rcid = models.IntegerField()
    session = models.ForeignKey('ProgramSchedule', db_column='session')
    ispresent = models.CharField(db_column='isPresent', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'attendance'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class CertificateAudit(models.Model):
    workshopid = models.IntegerField()
    rcid = models.ForeignKey('Remotecenter', db_column='rcid')
    dispatch = models.TextField()
    time = models.DateTimeField()
    updated_by = models.ForeignKey('Person', db_column='updated_by')

    class Meta:
        managed = False
        db_table = 'certificate_audit'


class City(models.Model):
    cityid = models.AutoField(primary_key=True)
    stateid = models.ForeignKey('State', db_column='stateid', blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    isactive = models.IntegerField(db_column='isActive', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'city'


class CoRegistration(models.Model):
    regi_id = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    mobile_no = models.CharField(max_length=11, blank=True, null=True)
    rcid = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=120, blank=True, null=True)
    middle_name = models.CharField(max_length=120, blank=True, null=True)
    surname = models.CharField(max_length=120, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    address_line1 = models.CharField(max_length=120, blank=True, null=True)
    address_line2 = models.CharField(max_length=120, blank=True, null=True)
    pin_code = models.CharField(max_length=60, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=60, blank=True, null=True)
    designation = models.CharField(max_length=60, blank=True, null=True)
    quali_bache = models.CharField(max_length=60, blank=True, null=True)
    quali_bache_other = models.CharField(max_length=60, blank=True, null=True)
    quali_master = models.CharField(max_length=60, blank=True, null=True)
    quali_master_other = models.CharField(max_length=60, blank=True, null=True)
    doc_degree = models.CharField(max_length=60, blank=True, null=True)
    exp_year = models.IntegerField(blank=True, null=True)
    exp_month = models.IntegerField(blank=True, null=True)
    signals_systems = models.CharField(max_length=60, blank=True, null=True)
    digital_signal = models.CharField(max_length=60, blank=True, null=True)
    network_theory = models.CharField(max_length=60, blank=True, null=True)
    control_systems = models.CharField(max_length=60, blank=True, null=True)
    date_time = models.CharField(max_length=60, blank=True, null=True)
    locked = models.CharField(max_length=10, blank=True, null=True)
    regstatus = models.CharField(max_length=10, blank=True, null=True)
    permission_letter = models.CharField(max_length=240, blank=True, null=True)
    uid = models.CharField(max_length=100, blank=True, null=True)
    bank_file_upload = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    user_type = models.CharField(max_length=200, blank=True, null=True)
    total_seat = models.IntegerField(blank=True, null=True)
    accomodation = models.CharField(max_length=100, blank=True, null=True)
    no_of_participants = models.CharField(max_length=30, blank=True, null=True)
    exist = models.CharField(max_length=1, blank=True, null=True)
    contextid = models.IntegerField(blank=True, null=True)
    personid = models.IntegerField(blank=True, null=True)
    participantid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'co_registration'


class Contactus(models.Model):
    contact_name = models.CharField(max_length=40)
    contact_email = models.CharField(max_length=50)
    message = models.CharField(max_length=200)
    submitted_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'contactus'


class Context(models.Model):
    idcontext = models.IntegerField(primary_key=True)
    email = models.CharField(unique=True, max_length=80, blank=True, null=True)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    city = models.IntegerField(blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    homephone = models.CharField(max_length=15, blank=True, null=True)
    login_name = models.CharField(max_length=20, blank=True, null=True)
    email_verified = models.IntegerField(blank=True, null=True)
    mobile_verified = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'context'


class CourseAssessments(models.Model):
    assess_id = models.AutoField(primary_key=True)
    comp_id = models.IntegerField(blank=True, null=True)
    grader_type = models.CharField(max_length=100, blank=True, null=True)
    display_name = models.CharField(max_length=100, blank=True, null=True)
    display_order = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_assessments'


class CourseComponents(models.Model):
    comp_id = models.AutoField(primary_key=True)
    course_id = models.IntegerField(blank=True, null=True)
    category_code = models.IntegerField(blank=True, null=True)
    component_name = models.CharField(max_length=100, blank=True, null=True)
    display_order = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_components'


class CourseGraderTypes(models.Model):
    grader_id = models.AutoField(primary_key=True)
    course_id = models.IntegerField(blank=True, null=True)
    category_code = models.IntegerField(blank=True, null=True)
    grader_type = models.CharField(max_length=100, blank=True, null=True)
    min_count = models.IntegerField(blank=True, null=True)
    drop_count = models.IntegerField(blank=True, null=True)
    individual_max_marks = models.IntegerField(blank=True, null=True)
    total_weight = models.IntegerField(blank=True, null=True)
    short_label = models.CharField(max_length=20, blank=True, null=True)
    display_order = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_grader_types'


class CourseGrades(models.Model):
    grade_id = models.AutoField(primary_key=True)
    course_id = models.IntegerField(blank=True, null=True)
    learner_type = models.CharField(max_length=100, blank=True, null=True)
    grade = models.CharField(max_length=50, blank=True, null=True)
    grade_cutoffs = models.CharField(max_length=20, blank=True, null=True)
    tag = models.TextField(blank=True, null=True)
    display_order = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_grades'


class Customkeyvaluefields(models.Model):
    workshopid = models.IntegerField()
    displayorder = models.SmallIntegerField()
    key = models.CharField(max_length=50)
    value = models.TextField()
    is_displayed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'customkeyvaluefields'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Downloads(models.Model):
    workshopid = models.IntegerField()
    session = models.CharField(max_length=30)
    video_name = models.CharField(max_length=150)
    file_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'downloads'


class EmailContentEmailTable(models.Model):
    file_name = models.CharField(unique=True, max_length=200)
    descr = models.CharField(unique=True, max_length=200)
    link = models.CharField(unique=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'email_content_email_table'


class FdpSelectionCriteria(models.Model):
    workshop_id = models.IntegerField()
    criteria = models.TextField()

    class Meta:
        managed = False
        db_table = 'fdp_selection_criteria'


class Feedback(models.Model):
    participant = models.ForeignKey('Participant', db_column='participant')
    workshop = models.ForeignKey('Workshops', db_column='workshop')
    af = models.ForeignKey('Person', db_column='af')
    feedback = models.TextField()

    class Meta:
        managed = False
        db_table = 'feedback'
        unique_together = (('participant', 'workshop', 'af'),)


class Generatepdfcode(models.Model):
    workshopid = models.IntegerField(blank=True, null=True)
    rcid = models.IntegerField(blank=True, null=True)
    generatecode = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    generated_by = models.IntegerField(blank=True, null=True)
    generated_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'generatepdfcode'


class Institute(models.Model):
    idinstitute = models.AutoField(db_column='idInstitute', primary_key=True)  # Field name made lowercase.
    institutename = models.CharField(db_column='Institutename', max_length=250, blank=True, null=True)  # Field name made lowercase.
    state = models.ForeignKey('State', db_column='state', blank=True, null=True)
    city = models.IntegerField(blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=450, blank=True, null=True)
    accredition = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    officephone = models.CharField(max_length=40, blank=True, null=True)
    isactive = models.IntegerField(db_column='isActive')  # Field name made lowercase.
    last_update = models.DateTimeField()
    last_updatedby = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'institute'


class Letter(models.Model):
    participantid = models.IntegerField(primary_key=True)
    workshopid = models.IntegerField(blank=True, null=True)
    letter = models.CharField(max_length=120, blank=True, null=True)
    verified = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'letter'


class Login(models.Model):
    login = models.ForeignKey(Context, primary_key=True)
    login_name = models.CharField(unique=True, max_length=75, blank=True, null=True)
    password = models.CharField(max_length=75, blank=True, null=True)
    usertypeid = models.CharField(max_length=75, blank=True, null=True)
    loginstatus = models.CharField(max_length=75)
    last_login = models.DateTimeField(blank=True, null=True)
    no_of_logins = models.IntegerField(blank=True, null=True)
    ipaddress = models.CharField(max_length=80, blank=True, null=True)
    username = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login'


class Logs(models.Model):
    log_id = models.AutoField(primary_key=True)
    ip_address = models.CharField(max_length=100)
    time_of_login = models.DateTimeField()
    user_id = models.IntegerField()
    browser_used = models.CharField(max_length=50)
    os_used = models.CharField(max_length=50)
    time_of_logout = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'logs'


class Lookups(models.Model):
    category = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=15, blank=True, null=True)
    description = models.CharField(max_length=240, blank=True, null=True)
    comment = models.CharField(max_length=50, blank=True, null=True)
    isactive = models.IntegerField(db_column='isActive')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lookups'
        unique_together = (('category', 'code'),)


class Pagelist(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=100, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    content = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    last_update = models.DateTimeField()
    last_updatedby = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pagelist'


class Participant(models.Model):
    participantid = models.AutoField(primary_key=True)
    contextid = models.ForeignKey(Context, db_column='contextid', blank=True, null=True)
    personid = models.ForeignKey('Person', db_column='personid', blank=True, null=True)
    experience = models.CharField(max_length=45, blank=True, null=True)
    qualification = models.CharField(max_length=50, blank=True, null=True)
    instituteid_streamid = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    regtime = models.DateTimeField()
    instituteid = models.IntegerField(blank=True, null=True)
    streamid = models.IntegerField(blank=True, null=True)
    eligible_for_certificate = models.CharField(max_length=20, blank=True, null=True)
    payment = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'participant'


class ParticipantMarks(models.Model):
    marks_id = models.AutoField(primary_key=True)
    workshopid = models.IntegerField(blank=True, null=True)
    category_code = models.IntegerField(blank=True, null=True)
    participantid = models.IntegerField(blank=True, null=True)
    grader_type = models.CharField(max_length=100, blank=True, null=True)
    percent_marks = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'participant_marks'


class Participantreasons(models.Model):
    workshopid = models.IntegerField(blank=True, null=True)
    participantid = models.ForeignKey(Participant, db_column='participantid', blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    reasons = models.TextField(blank=True, null=True)
    last_update = models.DateTimeField()
    update_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'participantreasons'


class Partuserdata(models.Model):
    userinterfaceid = models.AutoField(primary_key=True)
    workshopid = models.IntegerField(blank=True, null=True)
    rcid = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    firstname = models.CharField(max_length=45, blank=True, null=True)
    lastname = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    qualification = models.CharField(max_length=50, blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    discipline = models.CharField(max_length=50, blank=True, null=True)
    experience = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(db_column='Gender', max_length=50, blank=True, null=True)  # Field name made lowercase.
    homeaddress = models.CharField(max_length=450, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    mobileno = models.CharField(max_length=50, blank=True, null=True)
    contactno = models.CharField(max_length=15, blank=True, null=True)
    institutename = models.CharField(max_length=250, blank=True, null=True)
    titleid = models.IntegerField(blank=True, null=True)
    qualificationid = models.IntegerField(blank=True, null=True)
    designationid = models.IntegerField(blank=True, null=True)
    streamid = models.IntegerField(blank=True, null=True)
    instituteid = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    participanttype = models.CharField(max_length=30, blank=True, null=True)
    errormessage = models.TextField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    createdon = models.DateTimeField()
    lastupdatedby = models.IntegerField(blank=True, null=True)
    lastupdateon = models.DateTimeField()
    filename = models.CharField(max_length=100, blank=True, null=True)
    filename_id = models.IntegerField(blank=True, null=True)
    stateid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partuserdata'


class Paymentdetails(models.Model):
    uid = models.IntegerField(primary_key=True)
    userid = models.CharField(max_length=50, blank=True, null=True)
    reqid = models.CharField(max_length=50, blank=True, null=True)
    reqtype = models.CharField(max_length=20, blank=True, null=True)
    totalamt = models.CharField(max_length=50, blank=True, null=True)
    transid = models.CharField(max_length=50, blank=True, null=True)
    refno = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    trans_date = models.DateTimeField()
    trans_time = models.CharField(max_length=20, blank=True, null=True)
    provid = models.CharField(max_length=50, blank=True, null=True)
    msg = models.TextField(blank=True, null=True)
    workshopid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    purpose = models.CharField(max_length=200, blank=True, null=True)
    appid = models.CharField(max_length=100, blank=True, null=True)
    recon_date = models.DateTimeField()
    recon_time = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paymentdetails'


class Person(models.Model):
    personid = models.IntegerField(primary_key=True)
    title_id = models.IntegerField(blank=True, null=True)
    firstname = models.CharField(max_length=45, blank=True, null=True)
    lastname = models.CharField(max_length=45, blank=True, null=True)
    designation = models.IntegerField(blank=True, null=True)
    genderinfo = models.CharField(max_length=1, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=180, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    streamid = models.IntegerField(blank=True, null=True)
    instituteid = models.IntegerField(blank=True, null=True)
    experience = models.CharField(max_length=45, blank=True, null=True)
    qualification = models.CharField(max_length=50, blank=True, null=True)
    aadharid = models.CharField(max_length=12, blank=True, null=True)
    yearofbirth = models.IntegerField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    facultystatus = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person'


class PrincipalFacultyForWorkshop(models.Model):
    workshop_id = models.IntegerField()
    pf = models.ForeignKey(Login)

    class Meta:
        managed = False
        db_table = 'principal_faculty_for_workshop'


class ProfDetails(models.Model):
    prof_id = models.AutoField(primary_key=True)
    user_id = models.CharField(unique=True, max_length=100)
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prof_details'


class ProgramSchedule(models.Model):
    workshopid = models.IntegerField()
    date = models.DateField()
    sessionid = models.IntegerField()
    isactive = models.IntegerField(db_column='isActive', blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(blank=True, null=True)
    time_from = models.CharField(max_length=11, blank=True, null=True)
    time_to = models.CharField(max_length=11, blank=True, null=True)
    update_till = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'program_schedule'


class Remotecenter(models.Model):
    remotecenterid = models.IntegerField(primary_key=True)
    remotecentername = models.CharField(max_length=90, blank=True, null=True)
    state = models.ForeignKey('State', db_column='state', blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    district = models.CharField(max_length=45, blank=True, null=True)
    active = models.IntegerField()
    rating = models.IntegerField()
    instituteid = models.IntegerField(db_column='Instituteid')  # Field name made lowercase.
    email = models.CharField(max_length=100)
    status = models.CharField(max_length=10)
    last_updatedby = models.CharField(max_length=20)
    last_update = models.DateTimeField()
    autonomous = models.CharField(max_length=3, blank=True, null=True)
    acd_cal_startdate = models.TextField(blank=True, null=True)
    affiliated_university = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'remotecenter'


class Remotecentercapacity(models.Model):
    rcid = models.IntegerField()
    workshopid = models.IntegerField()
    available_seats = models.IntegerField()
    available_accomo = models.IntegerField()
    allotedrc = models.IntegerField()
    enrolled_status = models.CharField(max_length=10, blank=True, null=True)
    acco_cost = models.CharField(max_length=30, blank=True, null=True)
    food_cost = models.CharField(max_length=30, blank=True, null=True)
    is_rcc_enrolled = models.CharField(max_length=3, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    is_declined = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'remotecentercapacity'


class RemotecentercapacityDeleted(models.Model):
    rcid = models.ForeignKey(Remotecenter, db_column='rcid')
    workshopid = models.IntegerField()
    available_seats = models.IntegerField()
    available_accomo = models.IntegerField()
    allotedrc = models.IntegerField()
    loginid = models.IntegerField(blank=True, null=True)
    deleted_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'remotecentercapacity_deleted'


class RoleManageAccessingModule(models.Model):
    module_id = models.IntegerField()
    role_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'role_manage_accessing_module'
        unique_together = (('module_id', 'role_id'),)


class RoleManageAccessingPage(models.Model):
    page = models.ForeignKey('RoleManagePage')
    role = models.ForeignKey('RoleManageRole')

    class Meta:
        managed = False
        db_table = 'role_manage_accessing_page'
        unique_together = (('page_id', 'role_id'),)


class RoleManageAccessingTag(models.Model):
    role = models.ForeignKey('RoleManageRole')
    tag = models.ForeignKey('RoleManageTag')

    class Meta:
        managed = False
        db_table = 'role_manage_accessing_tag'
        unique_together = (('tag_id', 'role_id'),)


class RoleManageModule(models.Model):
    module_name = models.CharField(max_length=200)
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'role_manage_module'


class RoleManagePage(models.Model):
    page_name = models.CharField(max_length=200)
    is_active = models.IntegerField()
    module_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'role_manage_page'
        unique_together = (('module_id', 'page_name'),)


class RoleManageRole(models.Model):
    role_name = models.CharField(max_length=200)
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'role_manage_role'


class RoleManageTag(models.Model):
    tag_name = models.CharField(max_length=200)
    page = models.ForeignKey(RoleManagePage)
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'role_manage_tag'
        unique_together = (('page_id', 'tag_name'),)


class State(models.Model):
    stateid = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=45, blank=True, null=True)
    isactive = models.IntegerField(db_column='isActive', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'state'


class StatusMatrix(models.Model):
    initialstatus = models.CharField(db_column='InitialStatus', max_length=30, blank=True, null=True)  # Field name made lowercase.
    registered = models.CharField(db_column='Registered', max_length=5, blank=True, null=True)  # Field name made lowercase.
    invalid = models.CharField(db_column='Invalid', max_length=5, blank=True, null=True)  # Field name made lowercase.
    approved = models.CharField(db_column='Approved', max_length=5, blank=True, null=True)  # Field name made lowercase.
    confirmed = models.CharField(db_column='Confirmed', max_length=5, blank=True, null=True)  # Field name made lowercase.
    completed = models.CharField(db_column='Completed', max_length=5, blank=True, null=True)  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'status_matrix'


class UploadedF2FMarks(models.Model):
    marks_id = models.AutoField(primary_key=True)
    workshopid = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=100, blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    updated_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'uploaded_f2f_marks'


class Uploadfiles(models.Model):
    filename = models.CharField(max_length=200, blank=True, null=True)
    update_by = models.IntegerField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'uploadfiles'


class Uploadscannedattendancedetails(models.Model):
    workshopid = models.IntegerField(blank=True, null=True)
    rcid = models.IntegerField(blank=True, null=True)
    filename = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    updated_by = models.IntegerField(blank=True, null=True)
    updated_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'uploadscannedattendancedetails'


class Visitorlog(models.Model):
    visitorid = models.AutoField(primary_key=True)
    time = models.DateTimeField()
    ipaddress = models.CharField(db_column='ipAddress', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'visitorlog'


class Visitorlogorig(models.Model):
    visitorid = models.IntegerField()
    time = models.DateTimeField()
    ipaddress = models.CharField(db_column='ipAddress', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'visitorlogorig'


class WorkshopCoordinator(models.Model):
    workshopid = models.IntegerField()
    rcid = models.IntegerField()
    name = models.CharField(max_length=50, blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=75, blank=True, null=True)
    contextid = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workshop_coordinator'


class WorkshopSelectionCriteria(models.Model):
    workshopid = models.IntegerField(unique=True)
    criteria = models.TextField()

    class Meta:
        managed = False
        db_table = 'workshop_selection_criteria'


class Workshops(models.Model):
    workshopid = models.IntegerField(primary_key=True)
    workshopname = models.TextField()
    categorycode = models.IntegerField()
    author = models.TextField(blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    objectives = models.TextField(blank=True, null=True)
    eventstatus = models.TextField(blank=True, null=True)
    eventdetailspagepath = models.TextField(blank=True, null=True)
    resourcepath = models.TextField(blank=True, null=True)
    coursewarestatus = models.TextField(blank=True, null=True)
    announcement = models.TextField(blank=True, null=True)
    whoshouldattend = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    certificatepath = models.TextField(blank=True, null=True)
    broucherpath = models.TextField(blank=True, null=True)
    mailcontentpath = models.TextField(blank=True, null=True)
    contact = models.TextField(blank=True, null=True)
    schedulepath = models.TextField(blank=True, null=True)
    sponsor = models.TextField(blank=True, null=True)
    howtoapply = models.TextField(blank=True, null=True)
    accomodation = models.TextField(blank=True, null=True)
    coursefee = models.TextField(blank=True, null=True)
    teachingfaculty = models.TextField(blank=True, null=True)
    durationandvenue = models.TextField(blank=True, null=True)
    lastdateforappli = models.TextField(blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    shrtintro = models.TextField(blank=True, null=True)
    shrtobj = models.TextField(blank=True, null=True)
    shrtbenefit = models.TextField(blank=True, null=True)
    contentupdate = models.IntegerField()
    startdateofappli = models.DateField()
    permissionletter = models.TextField()
    eligibility = models.TextField()
    respective_coordinatorid = models.IntegerField()
    permission_letter_ifrequired = models.IntegerField(blank=True, null=True)
    accomodation_ifavailable = models.IntegerField(blank=True, null=True)
    lms_moodle = models.IntegerField(db_column='LMS_Moodle', blank=True, null=True)  # Field name made lowercase.
    lms_iitbx = models.IntegerField(db_column='LMS_IITBx', blank=True, null=True)  # Field name made lowercase.
    iitbx_coursename = models.CharField(db_column='IITBx_coursename', max_length=150, blank=True, null=True)  # Field name made lowercase.
    moodle_coursename = models.CharField(db_column='Moodle_coursename', max_length=150, blank=True, null=True)  # Field name made lowercase.
    certificate_institute_wise = models.IntegerField()
    certificate_rc_wise = models.IntegerField()
    instructions = models.TextField(blank=True, null=True)
    certificate_criteria = models.TextField(blank=True, null=True)
    feeamount = models.CharField(max_length=100, blank=True, null=True)
    workshop_remark = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    datetobedisplayed = models.IntegerField(blank=True, null=True)
    workshop_is_pilot = models.IntegerField(blank=True, null=True)
    facetofaceintrif_available = models.IntegerField(blank=True, null=True)
    online_course_activityif_available = models.IntegerField(blank=True, null=True)
    collegeidcard_ifrequired = models.IntegerField(blank=True, null=True)
    dateif_tobedisplayed = models.IntegerField(blank=True, null=True)
    iitbx_coursekey = models.CharField(db_column='IITBx_coursekey', max_length=150, blank=True, null=True)  # Field name made lowercase.
    iitb_payment_if_required = models.IntegerField(blank=True, null=True)
    rc_payment_if_required = models.IntegerField(blank=True, null=True)
    workshop_by_invite = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workshops'


class WscNominations(models.Model):
    workshopid = models.IntegerField()
    rcid = models.IntegerField()
    coordinator_email = models.CharField(max_length=70)
    nominated_email = models.CharField(max_length=70)
    active_till = models.DateField()
    updated_by = models.IntegerField()
    updated_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wsc_nominations'
