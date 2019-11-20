# Generated by Django 2.1 on 2019-11-06 08:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_type_id', models.CharField(choices=[('1', '服务器'), ('2', '路由器'), ('3', '交换机'), ('4', '防火墙')], default='1', help_text='设备类型', max_length=1)),
                ('device_status_id', models.CharField(choices=[('1', '上架'), ('2', '在线'), ('3', '离线'), ('4', '下架')], default='1', help_text='设备状态', max_length=1)),
                ('cabinet', models.CharField(max_length=128, verbose_name='机柜')),
                ('name', models.CharField(max_length=128, verbose_name='设备名称')),
                ('latest_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='更新时间')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '资产表',
                'verbose_name_plural': '资产表',
                'db_table': 'asset',
            },
        ),
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='机柜编号')),
                ('latest_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='更新时间')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '机柜信息表',
                'verbose_name_plural': '机柜信息表',
                'db_table': 'cabinet',
            },
        ),
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=64, verbose_name='SSH用户')),
                ('password', models.CharField(max_length=1024, verbose_name='密码')),
                ('port', models.PositiveIntegerField(verbose_name='sshd监听端口号')),
                ('authed', models.BooleanField(default=False, help_text='是否建立了基于密钥的连接', verbose_name='是否认证')),
            ],
            options={
                'verbose_name': '连接表',
                'verbose_name_plural': '连接表',
                'db_table': 'connection',
            },
        ),
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.CharField(max_length=128, null=True, verbose_name='插槽号')),
                ('pd', models.CharField(max_length=128, null=True, verbose_name='接口类型')),
                ('raw', models.CharField(max_length=128, null=True, verbose_name='原始磁盘大小')),
                ('coreced', models.CharField(max_length=200, null=True, verbose_name='强制磁盘容量大小')),
            ],
            options={
                'verbose_name': '硬盘表',
                'verbose_name_plural': '硬盘表',
                'db_table': 'disk',
            },
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='机房名称')),
                ('addr', models.CharField(max_length=256, verbose_name='地址')),
                ('phone', models.CharField(max_length=11, verbose_name='联系电话')),
                ('latest_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='更新时间')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '机房信息表',
                'verbose_name_plural': '机房信息表',
                'db_table': 'idc',
            },
        ),
        migrations.CreateModel(
            name='InventoryPool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=128, verbose_name='组名')),
            ],
            options={
                'verbose_name': 'Ansible 资产管理表',
                'verbose_name_plural': 'Ansible 资产管理表',
                'db_table': 'inventory_pool',
            },
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.CharField(max_length=100, null=True, verbose_name='内存容量')),
                ('slot', models.CharField(max_length=128, null=True, verbose_name='插槽')),
                ('model', models.CharField(max_length=128, null=True, verbose_name='内存类型')),
                ('speed', models.CharField(max_length=128, null=True, verbose_name='速率')),
                ('manufacturer', models.CharField(max_length=128, null=True, verbose_name='内存厂商')),
                ('sn', models.CharField(max_length=128, null=True, verbose_name='产品序列号')),
            ],
            options={
                'verbose_name': '内存表',
                'verbose_name_plural': '内存表',
                'db_table': 'memory',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('os_name', models.CharField(max_length=520, verbose_name='操作系统')),
                ('machine', models.CharField(max_length=520, verbose_name='系统架构')),
                ('os_version', models.CharField(max_length=520, verbose_name='系统版本')),
                ('kernel', models.CharField(max_length=520, verbose_name='内核信息')),
                ('model_name', models.CharField(max_length=128, verbose_name='cpu名称')),
                ('cpu_type', models.CharField(max_length=128, verbose_name='cpu类型')),
                ('physical_count', models.IntegerField(verbose_name='cpu物理颗数')),
                ('physical_cores', models.IntegerField(verbose_name='每颗cpu核心数')),
                ('manager_ip', models.GenericIPAddressField(blank=True, default='', null=True, verbose_name='IP地址')),
                ('hostname', models.CharField(max_length=128, verbose_name='主机名')),
                ('asset', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server', to='cmdb.Asset', verbose_name='资产')),
                ('connection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server', to='cmdb.Connection', verbose_name='连接信息')),
            ],
            options={
                'verbose_name': '服务器表',
                'verbose_name_plural': '服务器表',
                'db_table': 'server',
            },
        ),
        migrations.CreateModel(
            name='SysUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='用户名')),
                ('user_type', models.CharField(choices=[('1', '超级管理员'), ('2', 'sudo 用户'), ('3', '普通用户')], default='3', max_length=1, verbose_name='用户类型')),
            ],
            options={
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
                'db_table': 'sys_users',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='标签')),
                ('latest_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='更新时间')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '标签信息表',
                'verbose_name_plural': '标签信息表',
                'db_table': 'tag',
            },
        ),
        migrations.CreateModel(
            name='TreeNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_name', models.CharField(max_length=128, verbose_name='节点名称')),
                ('node_upstream', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_node', to='cmdb.TreeNode', verbose_name='上级节点')),
            ],
            options={
                'verbose_name': '服务树节点表',
                'verbose_name_plural': '服务树节点表',
                'db_table': 'tree_node',
            },
        ),
        migrations.CreateModel(
            name='Variable2Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=64, verbose_name='变量名')),
                ('val', models.CharField(max_length=512, verbose_name='变量值')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inv2vars', to='cmdb.InventoryPool', verbose_name='所属组')),
            ],
            options={
                'verbose_name': 'Ansible 组变量表',
                'verbose_name_plural': 'Ansible 组变量表',
                'db_table': 'variable_group',
            },
        ),
        migrations.CreateModel(
            name='Variable2Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default='', max_length=64, verbose_name='变量名')),
                ('val', models.CharField(default='', max_length=512, verbose_name='变量值')),
                ('host', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server2vars', to='cmdb.Server', verbose_name='所属主机')),
            ],
            options={
                'verbose_name': 'Ansible 主机变量表',
                'verbose_name_plural': 'Ansible 主机变量表',
                'db_table': 'variable_host',
            },
        ),
        migrations.AddField(
            model_name='memory',
            name='server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memorys', to='cmdb.Server', verbose_name='服务器'),
        ),
        migrations.AddField(
            model_name='inventorypool',
            name='server',
            field=models.ManyToManyField(related_name='inventory', to='cmdb.Server', verbose_name='所属服务器'),
        ),
        migrations.AddField(
            model_name='disk',
            name='server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disks', to='cmdb.Server', verbose_name='服务器'),
        ),
        migrations.AddField(
            model_name='cabinet',
            name='idc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cabinet', to='cmdb.IDC', verbose_name='所属机房'),
        ),
        migrations.AddField(
            model_name='asset',
            name='node',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assets', to='cmdb.TreeNode', verbose_name='节点'),
        ),
    ]
